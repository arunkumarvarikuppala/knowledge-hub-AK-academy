import sqlite3
import hashlib
import hmac
import secrets
from pathlib import Path


# --------------------------------------------------
# DATABASE CONFIGURATION
# --------------------------------------------------

DB_PATH = Path(__file__).resolve().parent / "knowledgehub.db"

PASSWORD_ITERATIONS = 600_000


# --------------------------------------------------
# DATABASE CONNECTION
# --------------------------------------------------

def get_connection():
    """Create a connection to the SQLite database."""
    conn = sqlite3.connect(str(DB_PATH), timeout=10)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


# --------------------------------------------------
# PASSWORD SECURITY
# --------------------------------------------------

def hash_password(password):
    """Hash a password using PBKDF2-HMAC-SHA256."""

    salt = secrets.token_bytes(16)

    password_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt,
        PASSWORD_ITERATIONS
    )

    return f"{salt.hex()}${password_hash.hex()}"


def verify_password(password, stored_hash):
    """Verify a password against its stored hash."""

    try:
        salt_hex, expected_hash = stored_hash.split("$", 1)
        salt = bytes.fromhex(salt_hex)

        actual_hash = hashlib.pbkdf2_hmac(
            "sha256",
            password.encode("utf-8"),
            salt,
            PASSWORD_ITERATIONS
        ).hex()

        return hmac.compare_digest(actual_hash, expected_hash)

    except (ValueError, TypeError, AttributeError):
        return False


# --------------------------------------------------
# CREATE DATABASE TABLES
# --------------------------------------------------

def initialize_database():
    """Create all required tables if they do not exist."""

    with get_connection() as conn:

        # Teacher accounts
        conn.execute("""
            CREATE TABLE IF NOT EXISTS teachers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # Student accounts
        conn.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id TEXT UNIQUE NOT NULL,
                name TEXT NOT NULL,
                class_name TEXT NOT NULL
                    CHECK (class_name IN ('Class 9', 'Class 10')),
                password_hash TEXT NOT NULL,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # Examination results
        conn.execute("""
            CREATE TABLE IF NOT EXISTS exam_results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id TEXT NOT NULL,
                exam_name TEXT NOT NULL,
                subject TEXT NOT NULL,
                marks REAL NOT NULL CHECK (marks >= 0),
                total_marks REAL NOT NULL CHECK (total_marks > 0),
                exam_date TEXT DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (student_id)
                    REFERENCES students(student_id)
                    ON DELETE CASCADE,
                CHECK (marks <= total_marks)
            )
        """)

        # Useful indexes
        conn.execute("""
            CREATE INDEX IF NOT EXISTS idx_results_student
            ON exam_results(student_id)
        """)

        conn.execute("""
            CREATE INDEX IF NOT EXISTS idx_students_class
            ON students(class_name)
        """)


# --------------------------------------------------
# TEACHER ACCOUNT MANAGEMENT
# --------------------------------------------------
def migrate_exam_results():
    """Add exam_name to older exam_results tables if needed."""

    with get_connection() as conn:
        columns = {
            row["name"]
            for row in conn.execute(
                "PRAGMA table_info(exam_results)"
            ).fetchall()
        }

        if "exam_name" not in columns:
            conn.execute("""
                ALTER TABLE exam_results
                ADD COLUMN exam_name TEXT
            """)

            # Preserve compatibility with older records.
            if "exam_title" in columns:
                conn.execute("""
                    UPDATE exam_results
                    SET exam_name = exam_title
                    WHERE exam_name IS NULL
                """)

            elif "exam" in columns:
                conn.execute("""
                    UPDATE exam_results
                    SET exam_name = exam
                    WHERE exam_name IS NULL
                """)

            else:
                conn.execute("""
                    UPDATE exam_results
                    SET exam_name = 'Previous Examination'
                    WHERE exam_name IS NULL
                """)



def migrate_student_classes():
    """Safely widen the existing student class constraint to Classes 6-10.

    Existing student IDs, password hashes, and exam results are copied intact.
    Run this only after taking a backup of knowledgehub.db.
    """
    conn = get_connection()
    try:
        schema_row = conn.execute(
            "SELECT sql FROM sqlite_master WHERE type='table' AND name='students'"
        ).fetchone()
        schema = (schema_row["sql"] or "") if schema_row else ""
        if not schema or "Class 6" in schema:
            return
        # Only rebuild the legacy table when its old CHECK constraint is present.
        if "CHECK" not in schema.upper() or "Class 9" not in schema or "Class 10" not in schema:
            return

        result_columns = {r["name"] for r in conn.execute("PRAGMA table_info(exam_results)").fetchall()}
        student_columns = {r["name"] for r in conn.execute("PRAGMA table_info(students)").fetchall()}
        conn.commit()
        conn.execute("PRAGMA foreign_keys = OFF")
        conn.execute("BEGIN")
        conn.execute("""CREATE TABLE students_new (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id TEXT UNIQUE NOT NULL,
            name TEXT NOT NULL,
            class_name TEXT NOT NULL,
            password_hash TEXT NOT NULL,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )""")
        created = "created_at" if "created_at" in student_columns else "CURRENT_TIMESTAMP"
        conn.execute(f"""INSERT INTO students_new (id, student_id, name, class_name, password_hash, created_at)
            SELECT id, student_id, name, class_name, password_hash, {created} FROM students""")

        # Rebuild results as well so the foreign key points at the new students table.
        exam_expr = "exam_name" if "exam_name" in result_columns else ("exam_title" if "exam_title" in result_columns else ("exam" if "exam" in result_columns else "'Previous Examination'"))
        date_expr = "exam_date" if "exam_date" in result_columns else "CURRENT_TIMESTAMP"
        id_expr = "id" if "id" in result_columns else "NULL"
        conn.execute("""CREATE TABLE exam_results_new (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id TEXT NOT NULL,
            exam_name TEXT NOT NULL,
            subject TEXT NOT NULL,
            marks REAL NOT NULL CHECK (marks >= 0),
            total_marks REAL NOT NULL CHECK (total_marks > 0),
            exam_date TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (student_id) REFERENCES students_new(student_id) ON DELETE CASCADE,
            CHECK (marks <= total_marks)
        )""")
        required = {"student_id", "subject", "marks", "total_marks"}
        if required.issubset(result_columns):
            conn.execute(f"""INSERT INTO exam_results_new (id, student_id, exam_name, subject, marks, total_marks, exam_date)
                SELECT {id_expr}, student_id, COALESCE({exam_expr}, 'Previous Examination'), subject, marks, total_marks, {date_expr}
                FROM exam_results""")
        conn.execute("DROP TABLE exam_results")
        conn.execute("DROP TABLE students")
        conn.execute("ALTER TABLE students_new RENAME TO students")
        conn.execute("ALTER TABLE exam_results_new RENAME TO exam_results")
        conn.execute("CREATE INDEX IF NOT EXISTS idx_results_student ON exam_results(student_id)")
        conn.execute("CREATE INDEX IF NOT EXISTS idx_students_class ON students(class_name)")
        conn.commit()
        conn.execute("PRAGMA foreign_keys = ON")
    except Exception:
        conn.rollback()
        try:
            conn.execute("PRAGMA foreign_keys = ON")
        except Exception:
            pass
        raise
    finally:
        conn.close()


def delete_student(student_id):
    """Delete a student and their linked results after teacher confirmation."""
    student_id = str(student_id or "").strip()
    if not student_id:
        return False, "Choose a student first."
    with get_connection() as conn:
        found = conn.execute("SELECT student_id FROM students WHERE student_id = ?", (student_id,)).fetchone()
        if not found:
            return False, "Student was not found."
        conn.execute("DELETE FROM exam_results WHERE student_id = ?", (student_id,))
        conn.execute("DELETE FROM students WHERE student_id = ?", (student_id,))
    return True, f"Student {student_id} and their saved results were deleted."


def create_teacher(username, password):
    """Create a teacher account."""

    username = username.strip()

    if not username:
        return False, "Please enter a teacher username."

    if len(password) < 12:
        return False, "Teacher password must contain at least 12 characters."

    try:
        with get_connection() as conn:
            conn.execute("""
                INSERT INTO teachers (username, password_hash)
                VALUES (?, ?)
            """, (username, hash_password(password)))

        return True, "Teacher account created successfully."

    except sqlite3.IntegrityError:
        return False, "This teacher username already exists."


def authenticate_teacher(username, password):
    """Authenticate a teacher."""

    username = username.strip()

    with get_connection() as conn:
        teacher = conn.execute("""
            SELECT username, password_hash
            FROM teachers
            WHERE username = ?
        """, (username,)).fetchone()

    if teacher and verify_password(
        password,
        teacher["password_hash"]
    ):
        return {
            "username": teacher["username"]
        }

    return None


# --------------------------------------------------
# STUDENT ACCOUNT MANAGEMENT
# --------------------------------------------------

def create_student(student_id, name, class_name, password):
    """Register a student account."""

    student_id = student_id.strip()
    name = name.strip()
    class_name = class_name.strip()

    if not student_id or not name:
        return False, "Student ID and student name are required."

    if class_name not in tuple(f"Class {n}" for n in range(6, 11)):
        return False, "Please select a supported class from Class 6 to Class 10."

    if len(password) < 10:
        return False, "Student password must contain at least 10 characters."

    try:
        with get_connection() as conn:
            conn.execute("""
                INSERT INTO students (
                    student_id,
                    name,
                    class_name,
                    password_hash
                )
                VALUES (?, ?, ?, ?)
            """, (
                student_id,
                name,
                class_name,
                hash_password(password)
            ))

        return True, f"Student {name} registered successfully."

    except sqlite3.IntegrityError:
        return False, "This Student ID already exists."


def authenticate_student(student_id, password):
    """Authenticate a student."""

    student_id = student_id.strip()

    with get_connection() as conn:
        student = conn.execute("""
            SELECT student_id, name, class_name, password_hash
            FROM students
            WHERE student_id = ?
        """, (student_id,)).fetchone()

    if student and verify_password(
        password,
        student["password_hash"]
    ):
        # Never return the password hash to the UI.
        return {
            "student_id": student["student_id"],
            "name": student["name"],
            "class_name": student["class_name"]
        }

    return None


def get_all_students():
    """Return student records without password hashes."""

    with get_connection() as conn:
        students = conn.execute("""
            SELECT student_id, name, class_name, created_at
            FROM students
            ORDER BY class_name, name
        """).fetchall()

    return students


def get_student_by_id(student_id):
    """Find a student by Student ID."""

    with get_connection() as conn:
        student = conn.execute("""
            SELECT student_id, name, class_name, created_at
            FROM students
            WHERE student_id = ?
        """, (student_id.strip(),)).fetchone()

    return student


# --------------------------------------------------
# EXAMINATION RESULT MANAGEMENT
# --------------------------------------------------

def add_exam_result(
    student_id,
    exam_name,
    subject,
    marks,
    total_marks,
    exam_date=None
):
    """Save a student's examination result."""

    student_id = student_id.strip()
    exam_name = exam_name.strip()
    subject = subject.strip()

    if not student_id or not exam_name or not subject:
        return False, "Student ID, exam name and subject are required."

    try:
        marks = float(marks)
        total_marks = float(total_marks)
    except (ValueError, TypeError):
        return False, "Marks must be valid numbers."

    if total_marks <= 0:
        return False, "Total marks must be greater than zero."

    if marks < 0 or marks > total_marks:
        return False, "Marks must be between zero and total marks."

    try:
        with get_connection() as conn:

            student = conn.execute("""
                SELECT student_id
                FROM students
                WHERE student_id = ?
            """, (student_id,)).fetchone()

            if not student:
                return False, "Student ID was not found."

            if exam_date:
                conn.execute("""
                    INSERT INTO exam_results (
                        student_id,
                        exam_name,
                        subject,
                        marks,
                        total_marks,
                        exam_date
                    )
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (
                    student_id,
                    exam_name,
                    subject,
                    marks,
                    total_marks,
                    exam_date
                ))
            else:
                conn.execute("""
                    INSERT INTO exam_results (
                        student_id,
                        exam_name,
                        subject,
                        marks,
                        total_marks
                    )
                    VALUES (?, ?, ?, ?, ?)
                """, (
                    student_id,
                    exam_name,
                    subject,
                    marks,
                    total_marks
                ))

        return True, "Examination result saved successfully."

    except sqlite3.IntegrityError:
        return False, "Could not save the examination result."


def get_student_results(student_id=None):
    """
    Return results for one student.

    If student_id is None, return all results.
    """

    with get_connection() as conn:

        if student_id is None:
            results = conn.execute("""
                SELECT
                    er.id,
                    er.student_id,
                    s.name AS student_name,
                    s.class_name,
                    er.exam_name,
                    er.subject,
                    er.marks,
                    er.total_marks,
                    ROUND(
                        er.marks * 100.0 / er.total_marks,
                        2
                    ) AS percentage,
                    er.exam_date
                FROM exam_results er
                JOIN students s
                    ON s.student_id = er.student_id
                ORDER BY er.exam_date DESC, er.id DESC
            """).fetchall()

        else:
            results = conn.execute("""
                SELECT
                    id,
                    student_id,
                    exam_name,
                    subject,
                    marks,
                    total_marks,
                    ROUND(
                        marks * 100.0 / total_marks,
                        2
                    ) AS percentage,
                    exam_date
                FROM exam_results
                WHERE student_id = ?
                ORDER BY exam_date DESC, id DESC
            """, (student_id.strip(),)).fetchall()

    return results
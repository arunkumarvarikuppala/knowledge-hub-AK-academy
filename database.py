"""MongoDB Atlas storage for Knowledge Hub. Configure secrets outside source code.

Public application function signatures and password format match the SQLite version.
get_connection now yields a MongoDB Database, not a SQLite connection.
Requires a replica set (MongoDB Atlas) for multi-document transactions.
"""
import os
import math
import hashlib
import hmac
import secrets
from datetime import datetime, timezone
from contextlib import contextmanager
from functools import lru_cache
from pymongo import MongoClient, ReturnDocument
from pymongo.errors import DuplicateKeyError
from pymongo.read_concern import ReadConcern
from pymongo.write_concern import WriteConcern

PASSWORD_ITERATIONS = 600_000

def _setting(name):
    value = os.environ.get(name)
    if not value:
        import streamlit as st
        try:
            value = st.secrets.get(name)
        except FileNotFoundError:
            value = None
    if not isinstance(value, str) or not value.strip():
        raise RuntimeError(f"Configure {name} in Streamlit secrets or environment variables.")
    return value.strip()

@lru_cache(maxsize=1)
def _database():
    uri, name = _setting("MONGO_URI"), _setting("MONGO_DB_NAME")
    client = MongoClient(uri, serverSelectionTimeoutMS=10000, connectTimeoutMS=10000,
                         appname="KnowledgeHub", tz_aware=True)
    try:
        client.admin.command("ping")
    except Exception as exc:
        client.close()
        error_type = type(exc).__name__
        error_code = getattr(exc, "code", None)
        raise RuntimeError(
            f"MongoDB connection failed. Type: {error_type}; code: {error_code}. "
            "Check Atlas credentials and network access."
        ) from None
    return client[name]

@contextmanager
def get_connection():
    yield _database()

def _now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")

def _transaction(callback):
    db = _database()
    with db.client.start_session() as session:
        return session.with_transaction(lambda s: callback(db, s),
            read_concern=ReadConcern("snapshot"), write_concern=WriteConcern("majority"))

def _teacher_lock(db, session):
    # All teacher creation paths write this document before checking teachers.
    # Competing transactions conflict and retry with a fresh snapshot.
    db.metadata.update_one({"_id": "teacher_registration"}, {"$inc": {"revision": 1}}, session=session)

def initialize_database():
    db = _database()
    # Fail loudly on existing duplicates: never remove accounts to build indexes.
    db.teachers.create_index("username", unique=True, name="unique_teacher_username")
    db.students.create_index("student_id", unique=True, name="unique_student_id")
    db.students.create_index([("class_name", 1), ("name", 1)])
    db.exam_results.create_index([("student_id", 1), ("exam_date", -1)])
    db.exam_results.create_index("id", unique=True, name="unique_result_id")
    # Create collections used in transactions ahead of the first transaction.
    for key in ("teacher_registration", "result_counter"):
        try:
            db.metadata.update_one({"_id": key}, {"$setOnInsert": {"revision": 0}}, upsert=True)
        except DuplicateKeyError:
            pass

def migrate_exam_results():
    db = _database()
    db.exam_results.update_many({"$or": [{"exam_name": {"$exists": False}}, {"exam_name": None}]},
        [{"$set": {"exam_name": {"$ifNull": ["$exam_title", {"$ifNull": ["$exam", "Previous Examination"]}]}}}])

def migrate_student_classes():
    """MongoDB has no legacy SQLite class constraint; existing data stays intact."""
    return None



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

def create_teacher(username, password):
    """Create a teacher account."""

    username = username.strip()

    if not username:
        return False, "Please enter a teacher username."

    if len(password) < 12:
        return False, "Teacher password must contain at least 12 characters."

    password_hash = hash_password(password)
    def insert(db, session):
        _teacher_lock(db, session)
        db.teachers.insert_one({"username": username, "password_hash": password_hash,
                                "created_at": _now()}, session=session)
    try:
        _transaction(insert)
        return True, "Teacher account created successfully."
    except DuplicateKeyError:
        return False, "This teacher username already exists."


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
        _database().students.insert_one({"student_id": student_id, "name": name,
            "class_name": class_name, "password_hash": hash_password(password), "created_at": _now()})
        return True, f"Student {name} registered successfully."
    except DuplicateKeyError:
        return False, "This Student ID already exists."


def setup_first_teacher(username, password, supplied_key, configured_key):
    """Check the private setup key and atomically insert the initial teacher."""
    if not isinstance(configured_key, str) or len(configured_key) < 32:
        return False, "Teacher setup is disabled. Configure a random setup key of at least 32 characters."
    if not hmac.compare_digest(str(supplied_key).encode(), configured_key.encode()):
        return False, "Setup could not be completed. Check the setup key."
    username = username.strip()
    if not username or len(username) > 100 or len(password) < 12:
        return False, "Enter a username (1–100 characters) and a password of at least 12 characters."
    password_hash = hash_password(password)
    def insert(db, session):
        _teacher_lock(db, session)
        if db.teachers.find_one({}, session=session):
            return False, "Initial teacher setup is already complete. Please log in."
        db.teachers.insert_one({"username": username, "password_hash": password_hash,
                                "created_at": _now()}, session=session)
        return True, "Teacher account created. Log in using your new credentials."
    try:
        return _transaction(insert)
    except DuplicateKeyError:
        return False, "Initial teacher setup is already complete. Please log in."

def has_teacher():
    return _database().teachers.find_one({}, {"_id": 1}) is not None

def authenticate_teacher(username, password):
    teacher = _database().teachers.find_one({"username": username.strip()})
    if teacher and verify_password(password, teacher["password_hash"]):
        return {"username": teacher["username"]}
    return None

def authenticate_student(student_id, password):
    student = _database().students.find_one({"student_id": student_id.strip()})
    if student and verify_password(password, student["password_hash"]):
        return {key: student[key] for key in ("student_id", "name", "class_name")}
    return None

def get_all_students():
    return list(_database().students.find({}, {"_id": 0, "student_id": 1, "name": 1,
        "class_name": 1, "created_at": 1}).sort([("class_name", 1), ("name", 1)]))

def get_student_by_id(student_id):
    return _database().students.find_one({"student_id": student_id.strip()},
        {"_id": 0, "student_id": 1, "name": 1, "class_name": 1, "created_at": 1})

def delete_student(student_id):
    student_id = str(student_id or "").strip()
    if not student_id:
        return False, "Choose a student first."
    def remove(db, session):
        if not db.students.delete_one({"student_id": student_id}, session=session).deleted_count:
            return False, "Student was not found."
        db.exam_results.delete_many({"student_id": student_id}, session=session)
        return True, f"Student {student_id} and their saved results were deleted."
    return _transaction(remove)


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

    if not math.isfinite(marks) or not math.isfinite(total_marks):
        return False, "Marks must be finite numbers."

    if total_marks <= 0:
        return False, "Total marks must be greater than zero."

    if marks < 0 or marks > total_marks:
        return False, "Marks must be between zero and total marks."

    def insert(db, session):
        # Write the student so deletion and result insertion cannot race.
        student = db.students.update_one({"student_id": student_id},
            {"$inc": {"_result_revision": 1}}, session=session)
        if not student.matched_count:
            return False, "Student ID was not found."
        counter = db.metadata.find_one_and_update({"_id": "result_counter"},
            {"$inc": {"revision": 1}}, return_document=ReturnDocument.AFTER, session=session)
        db.exam_results.insert_one({"id": counter["revision"], "student_id": student_id,
            "exam_name": exam_name, "subject": subject, "marks": marks,
            "total_marks": total_marks, "exam_date": str(exam_date) if exam_date else _now()}, session=session)
        return True, "Examination result saved successfully."
    return _transaction(insert)


def get_student_results(student_id=None):
    db = _database()
    query = {} if student_id is None else {"student_id": student_id.strip()}
    results = []
    students = {s["student_id"]: s for s in get_all_students()} if student_id is None else {}
    for row in db.exam_results.find(query, {"_id": 0}).sort([("exam_date", -1), ("id", -1)]):
        if student_id is None:
            student = students.get(row["student_id"])
            if student is None:
                continue
            row.update(student_name=student["name"], class_name=student["class_name"])
        row["percentage"] = round(row["marks"] * 100.0 / row["total_marks"], 2)
        # Match the original public result columns exactly.
        keys = ["id", "student_id", "exam_name", "subject", "marks", "total_marks", "percentage", "exam_date"]
        if student_id is None:
            keys += ["student_name", "class_name"]
        results.append({key: row[key] for key in keys})
    return results


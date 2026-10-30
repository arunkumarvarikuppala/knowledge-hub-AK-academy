import streamlit as st
import html
from datetime import date, datetime, timedelta
import streamlit.components.v1 as components

from syllabus_data import EXTRA_SYLLABUS
from exam_data import EXAMS

from database import (
    initialize_database,
    migrate_exam_results,
    create_student,
    get_all_students,
    get_student_results,
    add_exam_result,
    delete_student,
    migrate_student_classes,
)
from auth import show_authentication, logout


# ======================================================
# PAGE CONFIGURATION AND DATABASE
# ======================================================

st.set_page_config(
    page_title="Knowledge Hub",
    page_icon="📚",
    layout="wide",
)

@st.cache_resource
def prepare_database():
    initialize_database()
    migrate_exam_results()
    migrate_student_classes()
    return True

prepare_database()


# ======================================================
# STYLING
# ======================================================

st.markdown(
    """
    <style>

    :root {
      --kh-ink:#f4f7ff; --kh-muted:#c1cce3; --kh-blue:#7da2ff; --kh-violet:#b49aff;
      --kh-panel:#182544; --kh-panel-border:#34466f;
    }
    html, body, [class*="css"] { font-family:'DM Sans',sans-serif; }
    .stApp {
      background:
        radial-gradient(ellipse at 10% 0%, rgba(56,189,248,.20), transparent 30%),
        radial-gradient(ellipse at 95% 8%, rgba(167,139,250,.20), transparent 30%),
        linear-gradient(145deg,#0b1224 0%,#101b35 52%,#17152f 100%);
      color:#f4f7ff;
    }
    [data-testid="stAppViewContainer"], [data-testid="stHeader"] { background:transparent !important; }
    [data-testid="stHeader"] { color:#f4f7ff; }
    h1,h2,h3,h4,h5,h6,p,li,label,.stMarkdown,.stText,.stCaption,
    [data-testid="stWidgetLabel"], [data-testid="stMarkdownContainer"] p,
    [data-testid="stMarkdownContainer"] li {
      color:#edf2ff;
    }
    h1,h2,h3 { font-family:'Manrope',sans-serif !important; letter-spacing:-.025em; }
    .main-title {
      font-family:'Manrope',sans-serif; font-size:clamp(30px,4vw,46px); font-weight:800;
      text-align:center; margin:6px 0 0; letter-spacing:-.04em;
      background:linear-gradient(100deg,#7dd3fc,#c4b5fd,#f9a8d4);
      -webkit-background-clip:text; -webkit-text-fill-color:transparent;
    }
    .subtitle { text-align:center; font-size:16px; color:#cbd5f5 !important; margin:4px 0 20px; }
    .kh-hero {
      padding:26px 28px; border-radius:24px; color:white;
      background:linear-gradient(120deg,#155e75 0%,#4338ca 56%,#7e22ce 100%);
      border:1px solid rgba(255,255,255,.16);
      box-shadow:0 18px 38px rgba(0,0,0,.24); margin:10px 0 22px; position:relative; overflow:hidden;
    }
    .kh-hero h2 { color:#fff !important; margin:0 0 8px; font-size:clamp(23px,3vw,34px); }
    .kh-hero p { color:#f1f5ff !important; margin:0; font-size:15px; }
    .kh-hero .orb { float:right; font-size:62px; filter:drop-shadow(0 8px 8px rgba(0,0,0,.22)); animation:floaty 3.4s ease-in-out infinite; margin-left:12px; }
    @keyframes floaty { 0%,100%{transform:translateY(0) rotate(-4deg)} 50%{transform:translateY(-7px) rotate(4deg)} }
    .kh-card {
      background:linear-gradient(145deg,#1d2d50,#172440); color:#f4f7ff;
      border:1px solid #3b4d78; border-radius:20px; padding:20px;
      box-shadow:0 9px 25px rgba(0,0,0,.20); min-height:130px; transition:transform .2s,box-shadow .2s;
    }
    .kh-card:hover { transform:translateY(-4px); box-shadow:0 16px 32px rgba(0,0,0,.30); border-color:#8b9fff; }
    .kh-icon { display:inline-flex; align-items:center; justify-content:center; width:52px; height:52px; border-radius:17px; font-size:28px; background:linear-gradient(135deg,#334d83,#514080); box-shadow:inset 0 1px 0 rgba(255,255,255,.18),0 5px 12px rgba(0,0,0,.18); margin-bottom:10px; }
    .kh-card-title { color:#fff !important; font-family:'Manrope',sans-serif; font-size:17px; font-weight:800; }
    .kh-card-text { color:#cbd5ee !important; font-size:13px; line-height:1.5; margin-top:5px; }
    div[data-testid="stMetric"] { background:linear-gradient(145deg,#1d2d50,#172440); border:1px solid #354873; border-radius:18px; padding:16px 18px; box-shadow:0 8px 22px rgba(0,0,0,.16); }
    div[data-testid="stMetricLabel"], div[data-testid="stMetricLabel"] p { color:#cbd5e1 !important; font-weight:600; }
    div[data-testid="stMetricValue"], div[data-testid="stMetricValue"] div { color:#a5c8ff !important; font-family:'Manrope',sans-serif; font-weight:800; }
    div.stButton > button, div.stFormSubmitButton > button {
      border-radius:12px; border:1px solid #6278b5; background:linear-gradient(135deg,#334b82,#55409a);
      color:#fff !important; font-weight:700; padding:.55rem 1rem; transition:transform .15s,box-shadow .15s;
    }
    div.stButton > button:hover, div.stFormSubmitButton > button:hover { transform:translateY(-1px); box-shadow:0 7px 16px rgba(0,0,0,.25); border-color:#b4c5ff; }
    div[data-testid="stTabs"] button { color:#dce6ff !important; font-weight:700; }
    div[data-testid="stTabs"] button[aria-selected="true"] { color:#fff !important; border-bottom-color:#8b9dff !important; }
    [data-testid="stSidebar"] { background:linear-gradient(180deg,#111d37,#17172f 70%,#201735) !important; border-right:1px solid #35466c; }
    [data-testid="stSidebar"] * { color:#edf2ff; }
    [data-testid="stTextInput"] input, [data-testid="stNumberInput"] input,
    [data-testid="stTextArea"] textarea, [data-baseweb="select"] > div,
    [data-testid="stDateInput"] input {
      background:#111c34 !important; color:#f8fafc !important;
      border-color:#52658f !important; caret-color:#fff;
    }
    input::placeholder, textarea::placeholder { color:#a8b5d0 !important; opacity:1 !important; }
    [data-baseweb="select"] * { color:#f8fafc !important; }
    [role="listbox"], [role="option"] { background:#172440 !important; color:#f8fafc !important; }
    [data-testid="stAlert"] { border-radius:14px; }
    [data-testid="stDataFrame"], [data-testid="stTable"] { border:1px solid #354873; border-radius:12px; overflow:hidden; }
    [data-testid="stExpander"] { background:rgba(29,45,80,.72); border:1px solid #354873; border-radius:12px; }
    .kh-footer { text-align:center; color:#aab8d4 !important; font-size:12px; padding:22px 0 8px; }
    hr { border-color:#35466c !important; }
    @media(max-width:700px){ .kh-hero{padding:20px;border-radius:18px}.kh-hero .orb{font-size:44px}.kh-card{padding:15px} }
    @media(max-width:700px){
      .block-container{padding:1rem .75rem 2rem !important}
      [data-testid="stHorizontalBlock"]{flex-wrap:wrap !important;gap:.6rem !important}
      [data-testid="stColumn"]{min-width:100% !important;flex:1 1 100% !important}
      button,input{min-height:44px}
      [role="tablist"]{overflow-x:auto;flex-wrap:nowrap}
      .kh-hero,.kh-card{box-shadow:none}.kh-hero .orb{animation:none}
      h1,h2,h3{overflow-wrap:anywhere}
    }
    @media(prefers-reduced-motion:reduce){*{animation:none !important;transition:none !important}}
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="main-title">✨ Knowledge Hub</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">by AK Academy · Learn Smart. Grow Strong. Achieve More.</div>',
    unsafe_allow_html=True,
)


# ======================================================
# OPENAI AI TUTOR
# ======================================================

def show_ai_tutor(user):
    st.subheader("🤖 Knowledge Hub AI Tutor")
    st.write("Ask questions about your subjects and get step-by-step explanations.")

    subject = st.selectbox(
        "Select Subject",
        [
            "Mathematics", "Physics", "Chemistry", "Biology",
            "English Language", "English Literature", "History & Civics",
            "Geography", "Computer Applications", "General Doubts",
        ],
        key="kh_subject",
    )
    language = st.selectbox(
        "Answer Language", ["English", "Telugu", "Hindi"], key="kh_language"
    )

    if "kh_ai_history" not in st.session_state:
        st.session_state["kh_ai_history"] = []

    for message in st.session_state["kh_ai_history"]:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    question = st.chat_input("Enter your question...", key="kh_question")
    if question:
        st.session_state["kh_ai_history"].append(
            {"role": "user", "content": question}
        )
        with st.chat_message("user"):
            st.markdown(question)

        try:
            from openai import OpenAI
            api_key = str(st.secrets.get("OPENAI_API_KEY", "")).strip()
            model = str(st.secrets.get("OPENAI_MODEL", "")).strip()
            if not api_key or not model:
                st.error("AI setup is incomplete. The app owner must add OPENAI_API_KEY and OPENAI_MODEL in Streamlit Cloud Settings → Secrets.")
                return
            client = OpenAI(api_key=api_key, timeout=60, max_retries=1)
            student_class = user.get("class_name", "ICSE school")
            system_prompt = f"""
You are Knowledge Hub AI Tutor for ICSE students.
Student class: {student_class}
Subject: {subject}
Answer language: {language}

Explain concepts in simple language. For mathematics, show formulas and
calculations step by step. Give examples when helpful. Encourage understanding.
Be honest if uncertain. Do not invent official syllabus requirements.
Respond in the selected language.
"""

            with st.chat_message("assistant"):
                with st.spinner("AI tutor is thinking..."):
                    response = client.responses.create(
                        model=model,
                        instructions=system_prompt,
                        input=st.session_state["kh_ai_history"][-10:],
                        max_output_tokens=2000,
                        store=False,
                    )

                    answer = response.output_text

                    if not answer:
                        answer = "Please try asking your question again."

                    st.markdown(answer)
            st.session_state["kh_ai_history"].append(
                {"role": "assistant", "content": answer}
            )
        except Exception as error:
            # Log safe diagnostics only; never include exception text or credentials.
            error_name = type(error).__name__
            status = getattr(error, "status_code", None)
            print("AI Tutor error:", error_name, "HTTP:", status)
            if isinstance(error, ModuleNotFoundError) and error.name == "openai":
                st.error("The OpenAI package is not installed on this deployment. App owner: commit requirements.txt containing openai beside app.py, check the connected branch and competing dependency files, and inspect the installation logs.")
            elif isinstance(error, ImportError):
                st.error("The AI library could not load. The app owner must check the deployment installation logs and OpenAI package version.")
            elif isinstance(error, FileNotFoundError) or error_name == "StreamlitSecretNotFoundError":
                st.error("OpenAI secrets are missing. The app owner must add OPENAI_API_KEY and OPENAI_MODEL in Streamlit Cloud Settings → Secrets.")
            elif error_name == "AuthenticationError":
                st.error("OpenAI rejected the API credentials. The app owner must check the private OPENAI_API_KEY in Cloud Secrets.")
            elif error_name == "RateLimitError":
                st.error("OpenAI reported a rate or quota limit. Wait before retrying; the app owner should check API billing, credits and usage limits.")
            elif error_name in ("NotFoundError", "PermissionDeniedError"):
                st.error("The requested OpenAI resource was unavailable or access was denied. The app owner should check OPENAI_MODEL and the API project's model permissions.")
            elif error_name in ("APIConnectionError", "APITimeoutError"):
                st.error("The app server could not reach OpenAI in time. Please try again shortly.")
            else:
                st.error("The OpenAI tutor could not complete the request. Please report this diagnostic code to the app owner: " + error_name)


    if st.button("🗑️ Clear Chat", key="kh_clear_chat"):
        st.session_state["kh_ai_history"] = []
        st.rerun()


# ======================================================
# TEACHER DASHBOARD
# ======================================================

def teacher_dashboard(user):
    st.markdown("<section class='kh-hero'><span class='orb'>🧑‍🏫</span><h2>Teacher Studio</h2><p>Manage learners, classes, marks and progress — all in one place.</p></section>", unsafe_allow_html=True)

    students = [dict(row) for row in (get_all_students() or [])]
    results = [dict(row) for row in (get_student_results() or [])]
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Students", len(students))
    col2.metric("Recorded Results", len(results))
    col3.metric("Platform", "Knowledge Hub")

    register_tab, students_tab, marks_tab, reports_tab = st.tabs(
        ["✨ Add Learner", "👥 Learners & Remove", "📝 Enter Marks", "🏆 Results"]
    )

    with register_tab:
        st.subheader("Register a New Student")
        with st.form("register_student"):
            student_id = st.text_input("Student Login ID")
            student_name = st.text_input("Student Full Name")
            class_name = st.selectbox("Class", [f"Class {n}" for n in range(6, 11)])
            password = st.text_input("Student Password", type="password")
            confirm_password = st.text_input("Confirm Password", type="password")
            submitted = st.form_submit_button("Register Student")

        if submitted:
            if not all([student_id.strip(), student_name.strip(), password, confirm_password]):
                st.error("Please complete every field.")
            elif password != confirm_password:
                st.error("Passwords do not match.")
            elif len(password) < 10:
                st.error("Use a password with at least 10 characters.")
            else:
                try:
                    created, message = create_student(student_id.strip(), student_name.strip(), class_name, password)
                    if created:
                        st.success(message)
                        st.rerun()
                    else:
                        st.error(message)
                except Exception as error:
                    print("Registration error:", type(error).__name__)
                    st.error("Could not register the learner. Check the details and try again.")

    with students_tab:
        st.subheader("Registered Students")
        students = [dict(row) for row in (get_all_students() or [])]
        if students:
            st.dataframe(students, use_container_width=True, hide_index=True)
            st.markdown("#### 🧹 Remove a learner")
            st.warning("Removing a learner also removes their saved examination results. This cannot be undone.")
            student_labels = {f"{s.get('name', 'Student')} · {s.get('student_id', '')} · {s.get('class_name', '')}": s.get('student_id') for s in students}
            selected_to_delete = st.selectbox("Choose learner to remove", list(student_labels.keys()), key="kh_delete_student_choice")
            confirm_delete = st.checkbox("I understand this deletes the learner account and linked results", key="kh_confirm_delete_student")
            if st.button("🗑️ Delete selected learner", type="secondary", disabled=not confirm_delete, key="kh_delete_student_button"):
                ok, message = delete_student(student_labels[selected_to_delete])
                if ok:
                    st.success(message)
                    st.rerun()
                else:
                    st.error(message)
        else:
            st.info("No learners registered yet. Use **Add Learner** to create the first account.")

    with marks_tab:
        st.subheader("Enter Examination Marks")
        students = [dict(row) for row in (get_all_students() or [])]
        if not students:
            st.info("Register a student before entering marks.")
        else:
            student_options = {}
            for student in students:
                login_id = student.get("student_id", "")
                if login_id:
                    name = student.get("name", "Student")
                    student_options[f"{name} ({login_id})"] = login_id

            if student_options:
                with st.form("exam_marks_form"):
                    selected_student = st.selectbox("Select Student", list(student_options.keys()))
                    exam_name = st.text_input("Examination Name", placeholder="Saturday Weekly Test")
                    subject = st.selectbox(
                        "Subject",
                        ["Mathematics", "Physics", "Chemistry", "Biology", "English",
                         "History & Civics", "Geography", "Computer Applications"],
                    )
                    total_marks = st.number_input("Maximum Marks", min_value=1, max_value=1000, value=100)
                    marks_obtained = st.number_input(
                        "Marks Obtained", min_value=0, max_value=int(total_marks), value=0
                    )
                    exam_date = st.date_input("Examination Date", value=date.today())
                    save_marks = st.form_submit_button("Save Marks")

                if save_marks:
                    if not exam_name.strip():
                        st.error("Enter an examination name.")
                    else:
                        try:
                            save_result = add_exam_result(
                                student_options[selected_student],
                                exam_name.strip(),
                                subject,
                                float(marks_obtained),
                                float(total_marks),
                                exam_date.isoformat(),
                            )
                            if isinstance(save_result, tuple):
                                if save_result[0]:
                                    st.success(save_result[1])
                                else:
                                    st.error(save_result[1])
                            elif save_result:
                                st.success("Marks saved successfully!")
                            else:
                                st.error("The database did not confirm that the marks were saved.")
                        except Exception as error:
                            print("Marks error:", type(error).__name__)
                            st.error("Could not save marks. Check the add_exam_result() function in database.py.")

    with reports_tab:
        st.subheader("Results and Reports")
        results = [dict(row) for row in (get_student_results() or [])]
        if results:
            st.dataframe(results, use_container_width=True, hide_index=True)
        else:
            st.info("No examination results available.")


# ======================================================
# STARTER SYLLABUS CONTENT
# ======================================================

@st.cache_data(show_spinner=False)
def build_syllabus():
    syllabus = {
        "Class 9": {
            "Mathematics": {
                "Number Systems": {
                    "notes": """### Number Systems

A number system is a way of classifying numbers.

- **Natural numbers:** 1, 2, 3, 4, ...
- **Whole numbers:** 0, 1, 2, 3, ...
- **Integers:** Positive numbers, negative numbers, and zero.
- **Rational numbers:** Numbers expressible as p/q, where q ≠ 0.
- **Irrational numbers:** Numbers that cannot be expressed as a ratio of integers, such as √2.""",
                    "questions": [
                        "Give two examples of rational numbers.",
                        "Is √2 rational or irrational?",
                        "Write three integers less than zero.",
                        "Is every natural number a whole number?",
                        "Express 0.5 as a fraction.",
                    ],
                },
                "Polynomials": {
                    "notes": """### Polynomials

A polynomial is an algebraic expression made from variables, coefficients,
and non-negative integer powers. Examples: 2x + 3, x² + 5x + 6.

The **degree** is the highest power of the variable. In 3x² + 2x + 5,
the degree is 2, the coefficient of x is 2, and the constant term is 5.""",
                    "questions": [
                        "Find the degree of 3x² + 2x + 5.",
                        "Identify the coefficient of x in 7x + 4.",
                        "Is x² + 1 a polynomial?",
                        "Find the constant term in 4x² + 3x - 8.",
                        "Give an example of a cubic polynomial.",
                    ],
                },
                "Linear Equations": {
                    "notes": """### Linear Equations

A linear equation has a variable whose highest power is one.

Example: 2x + 4 = 10. Subtract 4 from both sides: 2x = 6.
Divide both sides by 2: x = 3. Always perform the same operation on both sides.""",
                    "questions": [
                        "Solve: x + 5 = 12.", "Solve: 2x = 18.",
                        "Solve: 3x + 4 = 16.", "Solve: 5x - 10 = 15.",
                        "Solve: 4x + 8 = 24.",
                    ],
                },
            },
            "Physics": {
                "Motion": {
                    "notes": """### Motion

Motion is a change in position over time relative to a reference point.
**Speed = Distance / Time**. **Average velocity = Displacement / Time**.
**Acceleration = Change in velocity / Time taken**.
SI units: distance metre (m), time second (s), speed m/s, acceleration m/s².""",
                    "questions": [
                        "Define speed.", "What is the SI unit of velocity?",
                        "A car travels 100 m in 5 s. Find its average speed.",
                        "What is the difference between distance and displacement?",
                        "Define acceleration.",
                    ],
                },
            },
            "Chemistry": {
                "Matter": {
                    "notes": """### Matter

Matter is anything that has mass and occupies space. Common states are solid,
liquid, and gas. Solids have a definite shape and volume; liquids have a
definite volume but take their container's shape; gases have neither.
Changes of state include melting, freezing, evaporation, condensation, and sublimation.""",
                    "questions": [
                        "Define matter.", "Name the three common states of matter.",
                        "What is melting?", "What is condensation?", "Give one example of a gas.",
                    ],
                },
            },
        },
        "Class 10": {
            "Mathematics": {
                "Quadratic Equations": {
                    "notes": """### Quadratic Equations

A quadratic equation is ax² + bx + c = 0, where a ≠ 0.
Example: x² - 5x + 6 = 0 → (x - 2)(x - 3) = 0, so x = 2 or x = 3.
Quadratic formula: x = (-b ± √(b² - 4ac)) / 2a.
The discriminant is D = b² - 4ac.""",
                    "questions": [
                        "Solve: x² - 7x + 12 = 0.", "Solve: x² - 9 = 0.",
                        "Solve: x² + 5x + 6 = 0.",
                        "Identify a, b, and c in 2x² + 3x - 5 = 0.",
                        "Find the discriminant of x² - 4x + 4 = 0.",
                    ],
                },
                "Arithmetic Progressions": {
                    "notes": """### Arithmetic Progressions (AP)

An AP is a sequence with a constant difference between consecutive terms.
Example: 2, 5, 8, 11, ... has first term a = 2 and common difference d = 3.
Nth term: aₙ = a + (n - 1)d.
Sum of first n terms: Sₙ = n/2 × [2a + (n - 1)d].""",
                    "questions": [
                        "Find the common difference of 3, 7, 11, 15, ...",
                        "Find the 10th term of 2, 5, 8, 11, ...",
                        "Find the first term and common difference of 10, 7, 4, 1, ...",
                        "Write the formula for the nth term of an AP.",
                        "Find the 5th term of 4, 9, 14, 19, ...",
                    ],
                },
            },
            "Physics": {
                "Force and Work": {
                    "notes": """### Force and Work

A force is a push or pull and is measured in newtons (N).
Work done: W = F × s × cos(θ). When force and displacement point in the
same direction, W = F × s. Work is measured in joules (J).""",
                    "questions": [
                        "Define force.", "What is the SI unit of force?",
                        "What is the SI unit of work?",
                        "Calculate work done by a 10 N force over 3 m in the same direction.",
                        "When is work done by a force zero?",
                    ],
                },
            },
            "Chemistry": {
                "Chemical Bonding": {
                    "notes": """### Chemical Bonding

Chemical bonding explains how atoms join to form molecules and compounds.
**Ionic bonding** usually involves transfer of electrons (example: NaCl).
**Covalent bonding** involves sharing electron pairs (example: H₂).
Atoms form bonds to reach more stable electronic arrangements.""",
                    "questions": [
                        "What is a chemical bond?", "Explain ionic bonding.",
                        "Explain covalent bonding.", "Give an example of an ionic compound.",
                        "Give an example of a covalent molecule.",
                    ],
                },
            },
        },
    }

    # Friendly starter packs for Classes 6-8. These are introductory examples,
    # not a claim to be the complete or official CISCE syllabus.
    starter = {
        "Mathematics": {"Whole Numbers & Factors": ("Learn place value, factors, multiples and divisibility. Example: factors of 12 are 1, 2, 3, 4, 6 and 12.", ["List all factors of 18.", "Write the first five multiples of 7.", "Is 29 prime or composite?"]), "Fractions & Decimals": ("A fraction represents part of a whole. Decimals use place value after the decimal point.", ["Simplify 6/12.", "Write 0.5 as a fraction.", "Add 1/4 + 1/4."])},
        "Science": {"Living Things": ("Living things grow, need energy, respond to their surroundings and reproduce.", ["Name three characteristics of living things.", "Give two examples of living things.", "Why do plants need sunlight?"]), "Matter Around Us": ("Matter has mass and occupies space. Common states are solid, liquid and gas.", ["Name the three common states of matter.", "Give one example of a liquid.", "What happens when ice melts?"])},
        "English": {"Reading & Writing": ("Practise reading carefully, identifying the main idea, and writing clear sentences with correct punctuation.", ["Write a sentence using 'because'.", "Identify the noun in: The little bird sings.", "Write three sentences about your favourite book."])},
        "Social Studies": {"Maps & Our World": ("Maps represent places. A compass shows directions: north, south, east and west.", ["Name the four main directions.", "What is a map key/legend?", "Why do we use maps?"])},
        "Computer Studies": {"Digital Basics": ("A computer accepts input, processes data, stores information and produces output.", ["Name two input devices.", "What is software?", "Give an example of an output device."])},
    }
    for level in (6, 7, 8):
        syllabus.setdefault(f"Class {level}", {subject: {chapter: {"notes": notes, "questions": questions} for chapter, (notes, questions) in chapters.items()} for subject, chapters in starter.items()})

    # Add the extra catalogue without replacing detailed lessons above.
    for class_name, subjects in EXTRA_SYLLABUS.items():
        syllabus.setdefault(class_name, {})
        for subject, chapters in subjects.items():
            syllabus[class_name].setdefault(subject, {})
            for chapter_name, chapter_data in chapters.items():
                syllabus[class_name][subject].setdefault(chapter_name, chapter_data)
    return syllabus


# ======================================================
# MOCK EXAMINATION
# ======================================================

def show_mock_examinations(user):
    st.subheader("📝 Knowledge Hub Mock Examinations")
    st.write("Attempt practice exams, submit written answers, check explanations, and track your marks.")

    student_class = str(user.get("class_name", "Class 9")).strip().lower()
    eligible_exams = {
        name: exam for name, exam in EXAMS.items()
        if str(exam.get("class", "")).strip().lower() == student_class
    }
    if not eligible_exams:
        st.info("No mock examinations are available for your class yet.")
        return

    selected_exam = st.selectbox(
        "Choose an examination", options=list(eligible_exams.keys()),
        key="kh_selected_exam",
    )
    exam = eligible_exams[selected_exam]

    st.markdown(f"### {selected_exam}")
    c1, c2, c3 = st.columns(3)
    c1.metric("Class", exam["class"])
    c2.metric("Subject", exam["subject"])
    c3.metric("Duration", f'{exam["duration_minutes"]} min')
    st.caption(
        f'{len(exam["questions"])} MCQs • '
        f'{len(exam["written_questions"])} written questions'
    )

    # Reset only when the selected test changes.
    if st.session_state.get("kh_started_exam") != selected_exam:
        st.session_state.pop("kh_exam_deadline", None)
        st.session_state.pop("kh_exam_submission", None)

    if st.button("🚀 Start / Restart Examination", key="kh_start_exam", type="primary"):
        st.session_state["kh_started_exam"] = selected_exam
        st.session_state["kh_exam_deadline"] = (
            datetime.now() + timedelta(minutes=int(exam["duration_minutes"]))
        )
        st.session_state.pop("kh_exam_submission", None)
        for key in list(st.session_state.keys()):
            if key.startswith("kh_mcq_") or key.startswith("kh_written_"):
                del st.session_state[key]
        st.rerun()

    exam_started = (
        st.session_state.get("kh_started_exam") == selected_exam
        and st.session_state.get("kh_exam_deadline") is not None
    )

    if not exam_started:
        st.info("Choose an examination and click **Start / Restart Examination** to begin.")
        return

    deadline = st.session_state["kh_exam_deadline"]
    remaining_seconds = max(0, int((deadline - datetime.now()).total_seconds()))
    deadline_timestamp = int(deadline.timestamp() * 1000)

    previous_submission = st.session_state.get("kh_exam_submission")
    already_submitted = (
        previous_submission is not None
        and previous_submission.get("exam_name") == selected_exam
    )

    # Show the live countdown only while this exam is still in progress.
    if not already_submitted:
        components.html(
            f"""
            <div style="padding:14px;border:2px solid #d9534f;border-radius:10px;
                        text-align:center;font-family:Arial,sans-serif;">
              <div style="font-size:16px;">⏳ Time remaining</div>
              <div id="kh-timer" style="font-size:30px;font-weight:bold;color:#d9534f;">
                Loading timer...
              </div>
            </div>
            <script>
              const deadline = {deadline_timestamp};
              const timer = document.getElementById("kh-timer");
              function updateTimer() {{
                const remaining = Math.max(0, Math.floor((deadline - Date.now()) / 1000));
                const minutes = Math.floor(remaining / 60);
                const seconds = remaining % 60;
                timer.textContent = remaining <= 0 ? "TIME OVER" :
                  String(minutes).padStart(2, "0") + ":" + String(seconds).padStart(2, "0");
              }}
              updateTimer();
              setInterval(updateTimer, 1000);
            </script>
            """,
            height=105,
        )

    if remaining_seconds == 0 and not already_submitted:
        st.warning("Your allotted time has expired. Submit your answers now; the attempt will be marked late.")
    if previous_submission and previous_submission.get("exam_name") == selected_exam:
        st.success("✅ This examination has already been submitted.")
    else:
        with st.form(key=f"kh_exam_form_{selected_exam}"):
            st.markdown("#### Part A — Multiple-choice questions")
            st.caption("Each MCQ is worth 1 mark.")
            mcq_answers = []
            for index, question in enumerate(exam["questions"]):
                st.markdown(f"**Q{index + 1}. {question['question']}**")
                answer = st.radio(
                    f"Choose your answer for Question {index + 1}",
                    options=question["options"], index=None,
                    key=f"kh_mcq_{selected_exam}_{index}",
                    label_visibility="collapsed",
                )
                mcq_answers.append(answer)

            st.markdown("#### Part B — Written-answer questions")
            st.caption("Written answers are saved in this attempt but are not included in the automatic MCQ score.")
            written_answers = []
            for index, question in enumerate(exam["written_questions"]):
                st.markdown(f"**Q{index + 1}. {question['question']}**")
                written_answers.append(
                    st.text_area(
                        f"Your written answer {index + 1}",
                        key=f"kh_written_{selected_exam}_{index}", height=120,
                    )
                )
            submitted = st.form_submit_button("📩 Submit Examination", type="primary")

        if submitted:
            mcq_score = sum(
                1 for index, question in enumerate(exam["questions"])
                if mcq_answers[index] == question["answer"]
            )
            total_mcqs = len(exam["questions"])
            late_submission = datetime.now() > deadline
            student_internal_id = user.get("student_id")
            saved_to_database = False

            if student_internal_id is not None:
                try:
                    save_result = add_exam_result(
                        student_internal_id, selected_exam, exam["subject"],
                        float(mcq_score), float(total_mcqs), date.today().isoformat(),
                    )
                    # database.add_exam_result returns (success, message).
                    if isinstance(save_result, tuple):
                        saved_to_database = bool(save_result[0])
                        if not saved_to_database:
                            st.error(f"Your answers were checked, but the result was not saved: {save_result[1]}")
                    else:
                        saved_to_database = bool(save_result)
                        if not saved_to_database:
                            st.error("Your answers were checked, but the database did not confirm that the result was saved.")
                except Exception as error:
                    print("Mock exam result save error:", type(error).__name__, str(error))
                    st.error("Answers were checked, but the result could not be saved. Please check the CMD window for the technical error.")
            else:
                st.error("Your student ID is missing. The result could not be saved.")

            st.session_state["kh_exam_submission"] = {
                "exam_name": selected_exam,
                "score": mcq_score,
                "total": total_mcqs,
                "mcq_answers": mcq_answers,
                "written_answers": written_answers,
                "late": late_submission,
                "saved": saved_to_database,
            }
            st.rerun()

    result = st.session_state.get("kh_exam_submission")
    if result and result.get("exam_name") == selected_exam:
        st.divider()
        st.subheader("📊 Your Examination Report")
        score = result["score"]
        total = result["total"]
        percentage = (score / total * 100) if total else 0
        c1, c2, c3 = st.columns(3)
        c1.metric("MCQ Score", f"{score}/{total}")
        c2.metric("Percentage", f"{percentage:.1f}%")
        c3.metric(
            "Written Answers",
            f'{sum(bool(a.strip()) for a in result["written_answers"])}/'
            f'{len(result["written_answers"])} answered',
        )
        if result["late"]:
            st.warning("This attempt was submitted after the timer expired.")
        if result["saved"]:
            st.success("Your MCQ result has been saved to My Results.")

        st.markdown("#### MCQ answers and explanations")
        for index, question in enumerate(exam["questions"]):
            student_answer = result["mcq_answers"][index]
            correct_answer = question["answer"]
            if student_answer == correct_answer:
                st.success(f"Q{index + 1}: Correct — {correct_answer}")
            else:
                st.error(f"Q{index + 1}: Your answer: {student_answer or 'Not answered'}")
                st.write(f"**Correct answer:** {correct_answer}")
            st.caption(question.get("explanation", "Review this concept in your notes."))

        st.markdown("#### Written answers and reference answers")
        for index, question in enumerate(exam["written_questions"]):
            st.markdown(f"**Q{index + 1}. {question['question']}**")
            answer = result["written_answers"][index]
            st.write("**Your answer:** " + (answer if answer.strip() else "Not answered"))
            with st.expander("View reference answer"):
                st.write(question.get("reference_answer", "Ask your teacher to add a reference answer."))

        st.info(
            "The saved mark currently covers MCQs only. Written answers are available "
            "for review but are not automatically graded. The countdown display does "
            "not forcibly submit the form when it reaches zero."
        )


# ======================================================
# STUDENT DASHBOARD
# ======================================================

def student_dashboard(user):
    st.markdown(f"<section class='kh-hero'><span class='orb'>🚀</span><h2>Welcome back, {html.escape(str(user.get('name', 'Learner')))}!</h2><p>Your learning adventure starts here. Explore, practise, ask questions and celebrate every improvement.</p></section>", unsafe_allow_html=True)

    card_cols = st.columns(4)
    card_data = [("📚", "Learn", "Explore class-wise chapters"), ("🤖", "Ask AI", "Understand difficult topics"), ("🎯", "Practise", "Build confidence with tests"), ("🏆", "Progress", "Track your achievements")]
    for col, (icon, title, detail) in zip(card_cols, card_data):
        with col:
            st.markdown(f"<div class='kh-card'><div class='kh-icon'>{icon}</div><div class='kh-card-title'>{title}</div><div class='kh-card-text'>{detail}</div></div>", unsafe_allow_html=True)
    st.write("")
    page = st.selectbox("Open learning page", ["📚 Learning Centre", "🤖 AI Doubt Solver", "🎯 Mock Exams", "🏆 My Results"], key="kh_page")

    if page == "📚 Learning Centre":
        st.subheader("📚 ICSE Learning Centre")
        academic_year = st.selectbox(
            "🎓 Choose the academic year", ["2026–27", "2027–28"],
            key="kh_academic_year",
        )
        st.info(
            f"Selected academic year: {academic_year}. The displayed catalogue is starter "
            "material and is not yet verified as a complete official CISCE syllabus."
        )
        st.write("Choose your class, subject, and chapter to start learning.")

        syllabus = build_syllabus()
        student_class = user.get("class_name", "Class 6")
        class_options = [f"Class {n}" for n in range(6, 11)]
        preferred_class = student_class if student_class in class_options else "Class 6"
        selected_class = st.selectbox(
            "🎓 Select Class", class_options,
            index=class_options.index(preferred_class),
            key="kh_syllabus_class",
        )
        available_subjects = syllabus[selected_class]
        selected_subject = st.selectbox(
            "📘 Select Subject", list(available_subjects.keys()),
            key="kh_syllabus_subject",
        )
        available_chapters = available_subjects[selected_subject]
        selected_chapter = st.selectbox(
            "📖 Select Chapter", list(available_chapters.keys()),
            key="kh_syllabus_chapter",
        )
        chapter = available_chapters[selected_chapter]
        st.divider()
        st.header(f"📖 {selected_chapter}")
        st.markdown(chapter["notes"])
        st.divider()
        st.subheader("✍️ Practice Questions")
        for number, question in enumerate(chapter["questions"], start=1):
            st.write(f"**Q{number}.** {question}")

        st.subheader("📝 Try Your Answer")
        st.text_area(
            "Write your answer to a practice question",
            key="kh_practice_answer",
            placeholder="Type your answer here...",
        )
        st.caption("Your practice answer is not graded or saved yet.")
        if st.button("🤖 Ask AI to Explain This Chapter", key="kh_chapter_ai"):
            st.session_state["kh_ai_history"] = [{
                "role": "user",
                "content": (
                    f"I'm studying {selected_class}, {selected_subject}, chapter "
                    f"'{selected_chapter}'. Teach me this chapter in simple steps, "
                    "explain important concepts, and give examples."
                ),
            }]
            st.info("Your chapter question is ready. Open the AI Doubt Solver tab to get the explanation.")

    if page == "🤖 AI Doubt Solver":
        show_ai_tutor(user)

    if page == "🎯 Mock Exams":
        show_mock_examinations(user)

    if page == "🏆 My Results":
        st.subheader("My Examination Results")
        student_internal_id = user.get("student_id")
        if student_internal_id is None:
            st.warning("The student database ID is missing from your login session. Check student authentication data.")
        else:
            try:
                my_results = [dict(row) for row in (get_student_results(student_internal_id) or [])]
                if my_results:
                    st.dataframe(my_results, use_container_width=True, hide_index=True)
                else:
                    st.info("Your results will appear here after your teacher records marks or you submit a mock examination.")
            except Exception as error:
                print("Student results error:", type(error).__name__)
                st.error("Could not load your results.")


# ======================================================
# MAIN
# ======================================================

def main():
    if "user" not in st.session_state:
        show_authentication()
        return

    user = st.session_state["user"]
    if user.get("role") == "teacher":
        st.warning("Storage: this version uses SQLite. On Streamlit Cloud, accounts and marks may be lost on reboot/redeployment. Use persistent hosting before storing real student records.")
    with st.sidebar:
        st.title("📚 Knowledge Hub")
        if user.get("role") == "teacher":
            st.write(f"Teacher: {user.get('username', 'Teacher')}")
        else:
            st.write(f"Student: {user.get('name', 'Student')}")
        st.divider()
        if st.button("🚪 Logout", use_container_width=True):
            logout()

    if user.get("role") == "teacher":
        teacher_dashboard(user)
    elif user.get("role") == "student":
        student_dashboard(user)
    else:
        st.error("Unknown account type. Please log in again.")
        if st.button("Return to Login"):
            logout()


if __name__ == "__main__":
    main()

st.markdown("<div class='kh-footer'>📚 Knowledge Hub by AK Academy · Learn Smart. Grow Strong. Achieve More. · © 2026 AK Academy · Made with ❤️ for young learners</div>", unsafe_allow_html=True)

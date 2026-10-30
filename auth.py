import streamlit as st
import time

from database import (
    authenticate_student,
    authenticate_teacher, has_teacher, setup_first_teacher
)


def show_authentication():
    st.markdown("<div style='text-align:center;font-size:54px;margin:6px 0 0'>🚀📚✨</div>", unsafe_allow_html=True)
    st.title("Knowledge Hub")
    st.markdown("<p style='text-align:center;color:#687590;font-size:17px'>by <b>AK Academy</b> · A brighter way to learn</p>", unsafe_allow_html=True)
    st.info("Choose your portal below. Students use the login ID and password shared by their teacher.")

    student_tab, teacher_tab = st.tabs([
        "🎓 Student Login",
        "👨‍🏫 Teacher Login"
    ])

    with student_tab:
        st.write("Login using the credentials provided by your teacher.")

        with st.form("student_login"):
            student_id = st.text_input("Student ID")
            password = st.text_input(
                "Password",
                type="password"
            )

            submitted = st.form_submit_button("Student Login")

        if submitted:
            student = _attempt_login(authenticate_student, student_id, password)

            if student:
                st.session_state["user"] = {
                    "role": "student",
                    **student
                }
                st.rerun()
            else:
                st.error("Invalid Student ID or password.")

    with teacher_tab:
        st.write("Teacher access")

        with st.form("teacher_login"):
            username = st.text_input(
                "Teacher username",
                value=""
            )

            password = st.text_input(
                "Teacher password",
                type="password"
            )

            submitted = st.form_submit_button("Teacher Login")

        if submitted:
            teacher = _attempt_login(authenticate_teacher, username, password)

            if teacher:
                st.session_state["user"] = {
                    "role": "teacher",
                    **teacher
                }
                st.rerun()
            else:
                st.error("Invalid teacher username or password.")


    if not has_teacher():
        with st.expander("First teacher setup"):
            st.caption("Only the academy owner with the private setup key can create the first teacher.")
            with st.form("first_teacher", clear_on_submit=True):
                setup_key = st.text_input("Private setup key", type="password")
                setup_username = st.text_input("New teacher username", max_chars=100)
                setup_password = st.text_input("New teacher password (12+ characters)", type="password")
                confirmation = st.text_input("Confirm new password", type="password")
                create = st.form_submit_button("Create first teacher")
            if create:
                if not _allowed():
                    st.error("Please wait before trying again.")
                elif setup_password != confirmation:
                    st.error("Passwords do not match.")
                else:
                    try:
                        configured_key = st.secrets.get("TEACHER_SETUP_KEY", "")
                    except FileNotFoundError:
                        configured_key = ""
                    ok, message = setup_first_teacher(setup_username, setup_password, setup_key, configured_key)
                    st.session_state["kh_auth_next"] = time.monotonic() + 3
                    if ok:
                        st.session_state["kh_setup_done"] = message
                        st.rerun()
                    st.error(message)
    if st.session_state.get("kh_setup_done"):
        st.success(st.session_state.pop("kh_setup_done"))


def _allowed():
    return time.monotonic() >= st.session_state.get("kh_auth_next", 0)


def _attempt_login(authenticate, username, password):
    if not _allowed():
        st.warning("Please wait a few seconds before trying again.")
        return None
    result = authenticate(username, password)
    st.session_state["kh_auth_next"] = time.monotonic() + (0 if result else 3)
    return result


def logout():
    for key in list(st.session_state):
        del st.session_state[key]
    st.rerun()

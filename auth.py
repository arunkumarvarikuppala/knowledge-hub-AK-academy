import streamlit as st

from database import (
    authenticate_student,
    authenticate_teacher
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
            student = authenticate_student(student_id, password)

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
                value="arunkumar"
            )

            password = st.text_input(
                "Teacher password",
                type="password"
            )

            submitted = st.form_submit_button("Teacher Login")

        if submitted:
            teacher = authenticate_teacher(username, password)

            if teacher:
                st.session_state["user"] = {
                    "role": "teacher",
                    **teacher
                }
                st.rerun()
            else:
                st.error("Invalid teacher username or password.")


def logout():
    st.session_state.pop("user", None)
    st.rerun()
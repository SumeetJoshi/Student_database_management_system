# streamlit_app.py
import streamlit as st
from db import add_student, add_marks

st.title("🎓 Student Progress Tracker")

# Use Streamlit session state to remember roll number
if "current_roll_no" not in st.session_state:
    st.session_state.current_roll_no = None

# Add student section (only ask once)
if st.session_state.current_roll_no is None:
    st.subheader("Enter Student Details")
    roll_no = st.number_input("Roll Number", min_value=1, step=1)
    name = st.text_input("Student Name")

    if st.button("Save Student"):
        add_student(roll_no, name)
        st.session_state.current_roll_no = roll_no  # Store roll number
        st.success(f"Student {name} added. Now enter marks.")
else:
    st.info(f"Adding marks for Roll No: {st.session_state.current_roll_no}")

    # Marks entry section
    st.subheader("Enter Marks")
    subject = st.text_input("Subject")
    marks = st.number_input("Marks", min_value=0, max_value=100, step=1)

    if st.button("Add Marks"):
        add_marks(st.session_state.current_roll_no, subject, marks)
        st.success(f"Marks for {subject} added!")

    # Option to reset and add new student
    if st.button("Add New Student"):
        st.session_state.current_roll_no = None  # Reset for next student

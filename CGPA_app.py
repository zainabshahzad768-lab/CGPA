import streamlit as st

st.set_page_config(page_title="GPA & CGPA Calculator", page_icon="🎓", layout="centered")

st.title("🎓 GPA & CGPA Calculator")
st.write("Use this app to calculate your GPA and CGPA easily!")

# --- GPA CALCULATOR ---
st.header("📘 GPA Calculator")

num_subjects = st.number_input("Enter number of subjects:", min_value=1, step=1)

if num_subjects:
    total_points = 0
    total_credits = 0

    for i in range(1, num_subjects + 1):
        st.subheader(f"Subject {i}")
        credit = st.number_input(f"Credit hours for Subject {i}:", min_value=1.0, step=0.5, key=f"credit_{i}")
        grade = st.number_input(f"Grade points earned in Subject {i}:", min_value=0.0, max_value=4.0, step=0.01, key=f"grade_{i}")
        total_points += credit * grade
        total_credits += credit

    if total_credits > 0:
        gpa = total_points / total_credits
        st.success(f"🎯 Your GPA is: **{gpa:.2f}**")
    else:
        st.warning("Please enter valid credit hours and grade points.")

st.markdown("---")

# --- CGPA CALCULATOR ---
st.header("🎓 CGPA Calculator")

num_semesters = st.number_input("Enter number of semesters:", min_value=1, step=1, key="num_semesters")

if num_semesters:
    total_gpa = 0

    for i in range(1, num_semesters + 1):
        gpa_value = st.number_input(f"GPA for Semester {i}:", min_value=0.0, max_value=4.0, step=0.01, key=f"gpa_{i}")
        total_gpa += gpa_value

    cgpa = total_gpa / num_semesters
    st.success(f"🏆 Your CGPA is: **{cgpa:.2f}**")

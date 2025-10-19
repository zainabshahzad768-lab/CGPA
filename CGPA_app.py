import streamlit as st

st.set_page_config(page_title="GPA & CGPA Calculator", page_icon="🎓", layout="centered")

st.title("🎓 GPA & CGPA Calculator")
st.write("Use this app to calculate your GPA and CGPA easily!")

# ==========================
# 📘 GPA CALCULATOR SECTION
# ==========================
st.header("📘 GPA Calculator")

num_subjects = st.number_input("Enter number of subjects:", min_value=1, step=1)

if num_subjects:
    total_points = 0
    total_credits = 0

    st.info("Enter credit hours and marks for each subject to get your GPA.")

    for i in range(1, num_subjects + 1):
        st.subheader(f"Subject {i}")
        credit = st.number_input(f"Credit hours for Subject {i}:", min_value=1.0, step=0.5, key=f"credit_{i}")
        marks = st.number_input(f"Marks for Subject {i} (0–100):", min_value=0.0, max_value=100.0, step=0.5, key=f"marks_{i}")

        # Convert marks → grade points (using simple scale)
        if marks >= 85:
            grade_point = 4.0
        elif marks >= 80:
            grade_point = 3.7
        elif marks >= 75:
            grade_point = 3.3
        elif marks >= 70:
            grade_point = 3.0
        elif marks >= 65:
            grade_point = 2.7
        elif marks >= 60:
            grade_point = 2.3
        elif marks >= 55:
            grade_point = 2.0
        elif marks >= 50:
            grade_point = 1.7
        else:
            grade_point = 0.0

        total_points += grade_point * credit
        total_credits += credit

    if total_credits > 0:
        gpa = total_points / total_credits
        st.success(f"🎯 Your GPA is: **{gpa:.2f}**")

st.markdown("---")

# ==========================
# 🎓 CGPA CALCULATOR SECTION
# ==========================
st.header("🎓 CGPA Calculator")

num_semesters = st.number_input("Enter number of semesters:", min_value=1, step=1, key="num_semesters")

if num_semesters:
    total_gpa = 0

    for i in range(1, num_semesters + 1):
        gpa_value = st.number_input(f"GPA for Semester {i}:", min_value=0.0, max_value=4.0, step=0.01, key=f"gpa_{i}")
        total_gpa += gpa_value

    cgpa = total_gpa / num_semesters
    st.success(f"🏆 Your CGPA is: **{cgpa:.2f}**")

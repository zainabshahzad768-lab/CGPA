import streamlit as st

st.set_page_config(page_title="GPA & CGPA Calculator", page_icon="🎓", layout="centered")

st.title("🎓 GPA & CGPA Calculator")

st.write("This app helps you calculate your GPA for each semester and overall CGPA easily!")

# Step 1: Number of semesters
num_semesters = st.number_input("Enter number of semesters:", min_value=1, step=1)

if num_semesters:
    semesters = []
    total_points = 0
    total_credits = 0

    for sem in range(1, num_semesters + 1):
        st.subheader(f"Semester {sem}")
        num_subjects = st.number_input(f"Number of subjects in Semester {sem}:", min_value=1, step=1, key=f"subs_{sem}")

        sem_points = 0
        sem_credits = 0

        for sub in range(1, num_subjects + 1):
            st.write(f"**Subject {sub}**")
            credit = st.number_input(f"Credit hours for Subject {sub}:", min_value=1.0, step=0.5, key=f"credit_{sem}_{sub}")
            grade_point = st.number_input(f"Grade point (out of 4) for Subject {sub}:", min_value=0.0, max_value=4.0, step=0.01, key=f"grade_{sem}_{sub}")

            sem_points += credit * grade_point
            sem_credits += credit

        if sem_credits > 0:
            sem_gpa = sem_points / sem_credits
            st.success(f"🎯 Semester {sem} GPA = {sem_gpa:.2f}")
            semesters.append(sem_gpa)

            total_points += sem_points
            total_credits += sem_credits

    if total_credits > 0:
        cgpa = total_points / total_credits
        st.subheader("🏆 Final Result")
        st.write(f"**Overall CGPA = {cgpa:.2f}**")

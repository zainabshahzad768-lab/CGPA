import streamlit as st

st.set_page_config(page_title="GPA & CGPA Calculator", layout="centered")

st.title("🎓 GPA & CGPA Calculator")

st.write("This app helps students calculate their GPA and CGPA easily.")

# --- GPA CALCULATION ---
st.header("Step 1: Calculate GPA for a Semester")

num_subjects = st.number_input("Enter the number of subjects:", min_value=1, step=1)

if num_subjects:
    grades = []
    credits = []
    
    st.subheader("Enter Grades and Credit Hours")
    st.info("Use grade points like: A=4.0, B+=3.5, B=3.0, C=2.5, etc.")
    
    for i in range(int(num_subjects)):
        col1, col2 = st.columns(2)
        with col1:
            grade = st.number_input(f"Grade Points for Subject {i+1}:", min_value=0.0, max_value=4.0, step=0.01)
        with col2:
            credit = st.number_input(f"Credit Hours for Subject {i+1}:", min_value=1.0, step=1.0)
        grades.append(grade)
        credits.append(credit)

    if st.button("Calculate GPA"):
        total_points = sum([g * c for g, c in zip(grades, credits)])
        total_credits = sum(credits)
        gpa = total_points / total_credits if total_credits else 0
        st.success(f"✅ Your GPA for this semester is: **{gpa:.2f}**")

# --- CGPA CALCULATION ---
st.header("Step 2: Calculate CGPA for All Semesters")

num_semesters = st.number_input("Enter total number of semesters completed:", min_value=1, step=1)

if num_semesters:
    sem_gpas = []
    sem_credits = []

    for i in range(int(num_semesters)):
        col1, col2 = st.columns(2)
        with col1:
            gpa = st.number_input(f"GPA of Semester {i+1}:", min_value=0.0, max_value=4.0, step=0.01)
        with col2:
            credits = st.number_input(f"Total Credits of Semester {i+1}:", min_value=1.0, step=1.0)
        sem_gpas.append(gpa)
        sem_credits.append(credits)

    if st.button("Calculate CGPA"):
        total_weighted_gpa = sum([g * c for g, c in zip(sem_gpas, sem_credits)])
        total_sem_credits = sum(sem_credits)
        cgpa = total_weighted_gpa / total_sem_credits if total_sem_credits else 0
        st.success(f"🎯 Your Overall CGPA is: **{cgpa:.2f}**")

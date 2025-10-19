import streamlit as st

# Title
st.title("🎓 GPA & CGPA Calculator")

st.write("This app helps you calculate your semester GPA and overall CGPA easily.")

# --- Step 1: Number of Subjects ---
num_subjects = st.number_input("Enter number of subjects in this semester:", min_value=1, step=1)

subjects = []
total_points = 0
total_credits = 0

# --- Step 2: Enter subject details ---
st.subheader("Enter subject details")
for i in range(int(num_subjects)):
    st.write(f"### Subject {i+1}")
    credit = st.number_input(f"Credit hours for Subject {i+1}:", min_value=1.0, step=0.5, key=f"credit{i}")
    grade = st.selectbox(
        f"Select grade for Subject {i+1}:",
        options=["A", "B+", "B", "C+", "C", "D", "F"],
        key=f"grade{i}"
    )

    # Grade points
    grade_points = {
        "A": 4.0,
        "B+": 3.5,
        "B": 3.0,
        "C+": 2.5,
        "C": 2.0,
        "D": 1.0,
        "F": 0.0
    }[grade]

    total_points += grade_points * credit
    total_credits += credit

# --- Step 3: Calculate GPA ---
if total_credits > 0:
    gpa = total_points / total_credits
    st.success(f"✅ Your GPA for this semester is: **{gpa:.2f}**")
else:
    gpa = 0

st.divider()

# --- Step 4: CGPA Calculation ---
st.subheader("CGPA Calculator")

num_semesters = st.number_input("Enter total number of semesters completed:", min_value=1, step=1)

sem_gpas = []
sem_credits = []

for i in range(int(num_semesters)):
    sgpa = st.number_input(f"Enter GPA for Semester {i+1}:", min_value=0.0, max_value=4.0, step=0.01, key=f"sgpa{i}")
    scredits = st.number_input(f"Total credits in Semester {i+1}:", min_value=1.0, step=1.0, key=f"scredit{i}")
    sem_gpas.append(sgpa)
    sem_credits.append(scredits)

if st.button("Calculate CGPA"):
    total_weighted = sum([sem_gpas[i] * sem_credits[i] for i in range(int(num_semesters))])
    total_credit = sum(sem_credits)
    if total_credit > 0:
        cgpa = total_weighted / total_credit
        st.success(f"🎯 Your overall CGPA is: **{cgpa:.2f}**")
    else:
        st.error("Please enter valid semester credits.")

st.info("Tip: GPA = Total Grade Points ÷ Total Credit Hours | CGPA = (Sum of GPA×Credits) ÷ Total Credits")

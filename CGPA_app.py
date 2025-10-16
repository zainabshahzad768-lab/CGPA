import streamlit as st

st.title("🎓 GPA and CGPA Calculator for Students")

# Ask how many semesters the student has
num_semesters = st.number_input("Enter number of semesters:", min_value=1, max_value=12, step=1)

semester_data = []

# Input details for each semester
for i in range(int(num_semesters)):
    st.subheader(f"Semester {i+1}")
    num_subjects = st.number_input(f"Number of subjects in Semester {i+1}", min_value=1, max_value=12, step=1, key=f"sub_{i}")

    subjects = []
    total_points = 0
    total_credits = 0

    # Input GPA and credit hours for each subject
    for j in range(int(num_subjects)):
        st.markdown(f"**Subject {j+1}**")
        grade_point = st.number_input(f"Enter GPA/Grade Point for Subject {j+1}", min_value=0.0, max_value=4.0, step=0.01, key=f"gp_{i}_{j}")
        credit_hours = st.number_input(f"Enter Credit Hours for Subject {j+1}", min_value=1.0, max_value=6.0, step=1.0, key=f"cr_{i}_{j}")

        subjects.append((grade_point, credit_hours))
        total_points += grade_point * credit_hours
        total_credits += credit_hours

    # Calculate semester GPA
    if total_credits > 0:
        semester_gpa = total_points / total_credits
    else:
        semester_gpa = 0.0

    semester_data.append({
        "semester": i + 1,
        "subjects": subjects,
        "sem_points": total_points,
        "sem_credits": total_credits,
        "sem_gpa": semester_gpa
    })

# Display semester GPAs and calculate overall CGPA
if st.button("Calculate CGPA"):
    st.header("📊 Results")

    total_all_points = 0
    total_all_credits = 0

    for s in semester_data:
        st.write(f"Semester {s['semester']}: GPA = {s['sem_gpa']:.2f}  |  Points = {s['sem_points']:.2f}  | Credits = {s['sem_credits']}")
        total_all_points += s["sem_points"]
        total_all_credits += s["sem_credits"]

    if total_all_credits > 0:
        overall_cgpa = total_all_points / total_all_credits
        st.success(f"🎯 Overall CGPA = {overall_cgpa:.2f}")
    else:
        st.warning("No valid data entered to calculate CGPA.")

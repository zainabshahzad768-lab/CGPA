import streamlit as st

st.title("🎓 Student GPA & CGPA Calculator")

st.write("This app helps students calculate GPA for each semester and overall CGPA.")

# Number of semesters
num_semesters = st.number_input("Enter total number of semesters:", min_value=1, max_value=12, value=4)

semester_gpas = []  # store GPA of each semester

# Loop through each semester
for sem in range(1, num_semesters + 1):
    st.subheader(f"📘 Semester {sem}")
    num_subjects = st.number_input(f"How many subjects in Semester {sem}?", min_value=1, max_value=10, value=6, key=f"subjects_{sem}")
    
    subject_grades = []
    for subj in range(1, num_subjects + 1):
        grade = st.number_input(f"Enter GPA for Subject {subj}:", min_value=0.0, max_value=4.0, step=0.01, key=f"grade_{sem}_{subj}")
        subject_grades.append(grade)
    
    # Auto calculate semester GPA when all values entered
    if all(g > 0 for g in subject_grades):
        semester_gpa = sum(subject_grades) / len(subject_grades)
        semester_gpas.append(semester_gpa)
        st.success(f"✅ Semester {sem} GPA = {semester_gpa:.2f}")
    else:
        st.info(f"Please enter all subject GPAs for Semester {sem} to calculate GPA.")

# Calculate overall CGPA automatically if at least one semester is complete
if semester_gpas:
    cgpa = sum(semester_gpas) / len(semester_gpas)
    st.divider()
    st.success(f"🎯 Your Overall CGPA after {len(semester_gpas)} semesters is: **{cgpa:.2f}**")
else:
    st.warning("Enter GPA values for at least one semester to calculate CGPA.")

st.divider()
st.info("""
### Example
- Semester 1 Subjects → 3.0, 3.2, 2.8 → GPA = 3.00  
- Semester 2 Subjects → 3.0, 3.4, 2.6 → GPA = 3.00  
- Semester 3 Subjects → 4.0, 3.8, 4.0 → GPA = 3.93  
- Semester 4 Subjects → 3, 4, 2, 3, 3, 3 → GPA = 3.00  
**CGPA = (3.00 + 3.00 + 3.93 + 3.00) / 4 = 3.23**
""")
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

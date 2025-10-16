import streamlit as st

st.title("🎓 Student GPA & CGPA Calculator")

st.write("This app helps students calculate GPA for each semester and overall CGPA.")

# Number of semesters
num_semesters = st.number_input("Enter total number of semesters:", min_value=1, max_value=12, value=4)

semester_gpas = []  # will store GPA of each semester

# Loop through each semester
for sem in range(1, num_semesters + 1):
    st.subheader(f"📘 Semester {sem}")
    num_subjects = st.number_input(f"How many subjects in Semester {sem}?", min_value=1, max_value=10, value=6, key=f"subjects_{sem}")
    
    subject_grades = []
    for subj in range(1, num_subjects + 1):
        grade = st.number_input(f"Enter GPA for Subject {subj}:", min_value=0.0, max_value=4.0, step=0.01, key=f"grade_{sem}_{subj}")
        subject_grades.append(grade)
    
    if st.button(f"Calculate Semester {sem} GPA", key=f"calc_{sem}"):
        valid_grades = [g for g in subject_grades if g > 0]
        if valid_grades:
            semester_gpa = sum(valid_grades) / len(valid_grades)
            st.success(f"Semester {sem} GPA = {semester_gpa:.2f}")
            semester_gpas.append(semester_gpa)
        else:
            st.warning("Please enter at least one GPA value for this semester.")

# Calculate overall CGPA
if st.button("Calculate Overall CGPA"):
    valid_sem_gpas = [g for g in semester_gpas if g > 0]
    if valid_sem_gpas:
        cgpa = sum(valid_sem_gpas) / len(valid_sem_gpas)
        st.success(f"Your Overall CGPA after {len(valid_sem_gpas)} semesters is: **{cgpa:.2f}**")
    else:
        st.warning("Please calculate at least one semester GPA first.")

st.divider()
st.info("""
### Example
- Semester 1 Subjects → 3.0, 3.2, 2.8 → GPA = 3.00  
- Semester 2 Subjects → 3.0, 3.4, 2.6 → GPA = 3.00  
- Semester 3 Subjects → 4.0, 3.8, 4.0 → GPA = 3.93  
- Semester 4 Subjects → 3, 4, 2, 3, 3, 3 → GPA = 3.00  
**CGPA = (3.00 + 3.00 + 3.93 + 3.00) / 4 = 3.23**
""")

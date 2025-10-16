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

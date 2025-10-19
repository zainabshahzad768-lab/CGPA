import streamlit as st

st.set_page_config(page_title="GPA & CGPA Calculator", page_icon="🎓", layout="centered")

st.title("🎓 GPA & CGPA Calculator")

st.write("""
This app helps students calculate their GPA and CGPA easily.  
Just enter your subjects, credit hours, and GPAs for each semester.
""")

# Step 1: Ask number of semesters
num_semesters = st.number_input("Enter number of semesters completed:", min_value=1, step=1)

# Create a list to store GPA and total credits for each semester
semesters = []

for i in range(int(num_semesters)):
    st.subheader(f"📘 Semester {i+1}")
    
    num_subjects = st.number_input(f"Enter number of subjects in Semester {i+1}:", min_value=1, step=1, key=f"subs_{i}")
    
    total_points = 0
    total_credits = 0

    for j in range(int(num_subjects)):
        st.markdown(f"**Subject {j+1}**")
        credit = st.number_input(f"Credit hours for Subject {j+1}:", min_value=1.0, step=0.5, key=f"credit_{i}_{j}")
        grade_point = st.number_input(f"Grade Point for Subject {j+1} (e.g., 4.0, 3.7, etc.):", min_value=0.0, max_value=4.0, step=0.1, key=f"gpa_{i}_{j}")
        
        total_points += credit * grade_point
        total_credits += credit

    # Calculate GPA for this semester
    if total_credits > 0:
        semester_gpa = total_points / total_credits
        st.success(f"✅ GPA for Semester {i+1}: {semester_gpa:.2f}")
        semesters.append((semester_gpa, total_credits))
    else:
        st.warning(f"Please enter valid credits for Semester {i+1}.")

# Step 2: Calculate CGPA
if st.button("Calculate CGPA"):
    if semesters:
        total_points_all = sum(gpa * credits for gpa, credits in semesters)
        total_credits_all = sum(credits for _, credits in semesters)
        cgpa = total_points_all / total_credits_all
        st.subheader(f"🎯 Your CGPA is: {cgpa:.2f}")
    else:
        st.error("Please enter semester data first.")

import streamlit as st

st.title("🎓 GPA & CGPA Calculator")

st.write("This app calculates your GPA for each semester and overall CGPA.")
st.write("👉 Enter the number of subjects, their credits, and your GPA for each semester.")

# Store all semester data
semesters = []

num_semesters = st.number_input("Enter number of semesters:", min_value=1, step=1)

for i in range(num_semesters):
    st.subheader(f"Semester {i+1}")
    num_subjects = st.number_input(f"Number of subjects in Semester {i+1}:", min_value=1, step=1, key=f"subs_{i}")
    
    credits = []
    gpa = st.number_input(f"Enter GPA for Semester {i+1} (only numeric value, e.g. 3.75):", min_value=0.0, max_value=4.0, step=0.01, key=f"gpa_{i}")
    
    # Ask total credits for the semester
    total_credits = st.number_input(f"Enter total credits for Semester {i+1}:", min_value=1.0, step=0.5, key=f"credits_{i}")
    
    # Store data for CGPA calculation
    semesters.append({"semester": i+1, "gpa": gpa, "credits": total_credits})

if st.button("Calculate CGPA"):
    total_points = sum(s["gpa"] * s["credits"] for s in semesters)
    total_credits = sum(s["credits"] for s in semesters)
    
    if total_credits > 0:
        cgpa = total_points / total_credits
        st.success(f"🎯 Your CGPA is: {cgpa:.2f}")
        
        # Display semester details
        for s in semesters:
            st.write(f"Semester {s['semester']}: GPA = {s['gpa']:.2f} | Credits = {s['credits']:.2f}")
    else:
        st.warning("Please enter valid credits for all semesters.")

import streamlit as st

st.title("🎓 Student GPA & CGPA Calculator")

st.write("Enter your semester GPAs to calculate your CGPA.")

# Number of semesters
num_semesters = st.number_input("Enter number of semesters completed:", min_value=1, max_value=12, value=4)

gpa_list = []
for i in range(1, num_semesters + 1):
    gpa = st.number_input(f"GPA of Semester {i}:", min_value=0.0, max_value=4.0, step=0.01)
    gpa_list.append(gpa)

if st.button("Calculate CGPA"):
    valid_gpas = [g for g in gpa_list if g > 0]
    if len(valid_gpas) > 0:
        cgpa = sum(valid_gpas) / len(valid_gpas)
        st.success(f"Your CGPA after {num_semesters} semesters is: **{cgpa:.2f}**")
    else:
        st.warning("Please enter at least one valid GPA.")

st.divider()

st.subheader("📘 Example Calculation")

st.write("""
Example:
- Semester 1 GPA: 3.0  
- Semester 2 GPA: 3.0  
- Semester 3 GPA: 4.0  
- Semester 4 Subject GPAs: 3, 4, 2, 3, 3, 3  
  → Semester 4 GPA = (3+4+2+3+3+3)/6 = 3.00  
**Final CGPA = (3 + 3 + 4 + 3) / 4 = 3.25**
""")

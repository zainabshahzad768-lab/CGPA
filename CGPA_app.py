import streamlit as st

st.title("🎓 Accurate GPA & CGPA Calculator (Supports different # of courses & credits)")

st.write("Enter grade points for each subject and its credit hours. If a subject has no credit info, leave credit as 1.")

# number of semesters
num_semesters = st.number_input("Total number of semesters:", min_value=1, max_value=12, value=4)

# store global totals
global_total_points = 0.0
global_total_credits = 0.0

# store semester summaries for display
semester_summaries = []

for sem in range(1, num_semesters + 1):
    st.header(f"Semester {sem}")
    num_subjects = st.number_input(f"Number of subjects in Semester {sem}:", min_value=1, max_value=20, value=6, key=f"num_subs_{sem}")

    sem_points = 0.0
    sem_credits = 0.0

    # for layout: two columns for grade and credit
    cols = st.columns((2, 1))
    with cols[0]:
        st.markdown("**Enter grade point for each subject (0.00 - 4.00)**")
    with cols[1]:
        st.markdown("**Credit hours for each subject** (default 1)")

    for subj in range(1, num_subjects + 1):
        # unique keys so Streamlit remembers inputs correctly
        gp_key = f"gp_s{sem}_sub{subj}"
        cr_key = f"cr_s{sem}_sub{subj}"

        cols = st.columns((2, 1))
        with cols[0]:
            grade_point = st.number_input(f"Semester {sem} - Subject {subj} grade point:", min_value=0.0, max_value=4.0, step=0.01, key=gp_key, value=0.0)
        with cols[1]:
            credit = st.number_input(f"Credit (S{sem} Sub{subj}):", min_value=0.0, max_value=10.0, step=0.5, key=cr_key, value=1.0)

        # accumulate (even if grade_point 0.0 — includes failed/zero-point subjects)
        sem_points += grade_point * credit
        sem_credits += credit

    # compute semester GPA if there are credits
    if sem_credits > 0:
        sem_gpa = sem_points / sem_credits
        st.success(f"Semester {sem} GPA = **{sem_gpa:.3f}**  (Total points: {sem_points:.2f}, Credits: {sem_credits:.1f})")
    else:
        sem_gpa = None
        st.warning(f"Semester {sem} has zero total credits — cannot compute GPA.")

    # add to global totals
    global_total_points += sem_points
    global_total_credits += sem_credits

    # save summary row
    semester_summaries.append({
        "semester": sem,
        "sem_points": sem_points,
        "sem_credits": sem_credits,
        "sem_gpa": sem_gpa
    })

st.divider()

# overall CGPA
if global_total_credits > 0:
    cgpa = global_total_points / global_total_credits
    st.success(f"🎯 Overall CGPA = **{cgpa:.3f}**  (Total points: {global_total_points:.2f}, Total credits: {global_total_credits:.1f})")
else:
    st.warning("No credits entered across all semesters — cannot compute CGPA.")

st.divider()

# Show a compact summary table
st.subheader("Summary by Semester")
for s in semester_summaries:
    if s["sem_gpa"] is not None:
        st.write(f"Semester {s['semester']}: GPA = {s['sem_gpa']:.3f}  |  Points = {s['sem_points']:.2f}  | Credits = {s['sem_credits']:.1f}")
    else:
        st.write(f"Semester {s['semester']}: GPA = N/A  |  Points = {s['sem_points']:.2f}  | Credits = {s_]()

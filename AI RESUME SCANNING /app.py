# app.py

import streamlit as st
from parser.resume_parser import extract_resume_data
from parser.job_parser import get_job_descriptions
from utils.skill_matcher import calculate_match_score

st.title("AI Resume Screener with SQL Job Matching")

# Upload resume
uploaded_resume = st.file_uploader("Upload your resume (PDF)", type=["pdf"])

# Get job descriptions from database
jobs = get_job_descriptions()
job_titles = sorted(set(job['role'] for job in jobs))


# Select job role
selected_job_title = st.selectbox("Select a job role to match", job_titles)

# Analyze button
if st.button("Analyze") and uploaded_resume:
    # Extract skills from resume
    resume_text = uploaded_resume.read()
    resume_skills = extract_resume_data(resume_text)

    # Get only the first job that matches the selected title
    job = next((job for job in jobs if job['role'] == selected_job_title), None)

    if job:
        # Clean and split required skills
        required_skills = [skill.strip() for skill in job['required_skills'].split(',')]

        # Calculate match score
        score = calculate_match_score(resume_skills, required_skills)
        st.success(f"Match Score for {selected_job_title}: {round(score * 100, 2)}%")

        # Identify missing skills
        missing_skills = set(required_skills) - set(resume_skills)
        if missing_skills:
            st.warning(f"Missing Skills: {', '.join(missing_skills)}")
        else:
            st.info("✅ You have all the required skills!")
    else:
        st.error("Selected job role not found in the database.")

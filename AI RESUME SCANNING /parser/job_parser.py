
import sqlite3
import os

def get_job_descriptions():
    # Dynamically find the absolute path to job_descriptions.db
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # goes to RESUME_SCREENING_AI/
    db_path = os.path.join(base_dir, "data", "job_descriptions.db")
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT role, required_skills FROM job_descriptions")
    jobs = [{'role': row[0], 'required_skills': row[1]} for row in cursor.fetchall()]
    conn.close()
    return jobs

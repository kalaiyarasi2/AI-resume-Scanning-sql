# create_job_db.py

import sqlite3
import os

# Ensure the directory exists
db_folder = "data"
os.makedirs(db_folder, exist_ok=True)

# Correct DB path
db_path = os.path.join(db_folder, "job_descriptions.db")

# Connect and create table
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS job_descriptions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    role TEXT NOT NULL,
    required_skills TEXT NOT NULL
)
""")

# Insert sample data
sample_jobs = [
    ("Python Developer", "python,sql,streamlit,spacy,pandas"),
    ("Data Analyst", "excel,sql,powerbi,python,statistics"),
    ("ML Engineer", "python,scikit-learn,tensorflow,numpy,pandas"),
]

cursor.executemany("INSERT INTO job_descriptions (role, required_skills) VALUES (?, ?)", sample_jobs)
conn.commit()
conn.close()

print(f"✅ Database created at {db_path} and sample jobs inserted.")

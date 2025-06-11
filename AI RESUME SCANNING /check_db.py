# check_db.py

import sqlite3

db_path = "data/job_descriptions.db"

try:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print("Tables:", tables)

    if any("job_descriptions" in t for t in tables):
        print("✅ 'job_descriptions' table FOUND.")
    else:
        print("❌ 'job_descriptions' table NOT FOUND.")

except sqlite3.OperationalError as e:
    print("❌ Database error:", e)

finally:
    if conn:
        conn.close()

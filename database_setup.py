import sqlite3

# Connect to SQLite
conn = sqlite3.connect("attendance.db")
cursor = conn.cursor()

# Create table for students
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    student_id TEXT PRIMARY KEY,
    name TEXT,
    image_path TEXT
)
""")

# Create table for attendance
cursor.execute("""
CREATE TABLE IF NOT EXISTS attendance (
    student_id TEXT,
    date TEXT,
    status TEXT,
    PRIMARY KEY(student_id, date)
)
""")

conn.commit()
conn.close()
print("Database created successfully!")

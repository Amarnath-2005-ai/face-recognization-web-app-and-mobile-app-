import sqlite3

def add_student(student_id, name, image_path):
    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()
    cursor.execute("INSERT OR REPLACE INTO students (student_id, name, image_path) VALUES (?, ?, ?)",
                   (student_id, name, image_path))
    conn.commit()
    conn.close()
    print(f"Added {name} to database")

# # Example usage
add_student("03", "Amarnath Ghosh", "faces_db/a.jpg")
add_student("13", "Debjit Goswami", "faces_db/d.jpg")
add_student("05","Asmita Ghosh","faces_db/b.jpg")
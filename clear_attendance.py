import sqlite3

def clear_attendance():
    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM attendance")  # Delete all records
    conn.commit()
    conn.close()
    print("✅ All attendance records have been cleared!")

if __name__ == "__main__":
    clear_attendance()

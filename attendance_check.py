from deepface import DeepFace
from mtcnn import MTCNN
import cv2
import sqlite3
from datetime import datetime
import os

detector = MTCNN()  # Lightweight face detector

def detect_face(img_path):
    img = cv2.imread(img_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    faces = detector.detect_faces(img_rgb)
    if faces:
        x, y, w, h = faces[0]['box']
        face = img_rgb[y:y+h, x:x+w]
        temp_face_path = os.path.join("uploads", "temp_face.jpg")
        face_bgr = cv2.cvtColor(face, cv2.COLOR_RGB2BGR)
        cv2.imwrite(temp_face_path, face_bgr)
        return temp_face_path
    else:
        return None

def check_and_mark_attendance(uploaded_image):
    cropped_face = detect_face(uploaded_image)
    if cropped_face is None:
        return "❌ No face detected"

    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()
    cursor.execute("SELECT student_id, name, image_path FROM students")
    students = cursor.fetchall()

    for student_id, name, image_path in students:
        try:
            result = DeepFace.verify(cropped_face, image_path, model_name="Facenet", enforce_detection=False)
            if result["verified"]:
                date_str = datetime.now().strftime("%Y-%m-%d")
                cursor.execute("INSERT OR IGNORE INTO attendance (student_id, date, status) VALUES (?, ?, ?)",
                               (student_id, date_str, "Present"))
                conn.commit()
                conn.close()
                return f"✅ Attendance marked for {name}"
        except:
            continue

    conn.close()
    return "❌ Face not recognized in database"

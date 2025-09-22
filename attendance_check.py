from deepface import DeepFace
from mtcnn import MTCNN
import cv2
import numpy as np
import sqlite3
from datetime import datetime
import os

detector = MTCNN()  # Lightweight face detector

def enhance_low_light(image):
    # Convert to LAB color space for better lighting adjustment
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    
    # Apply CLAHE to L channel (lightness)
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
    l = clahe.apply(l)
    
    # Merge channels and convert back to BGR
    enhanced_lab = cv2.merge([l, a, b])
    enhanced_bgr = cv2.cvtColor(enhanced_lab, cv2.COLOR_LAB2BGR)
    
    # Additional gamma correction for very dark images
    gamma = 1.2
    enhanced_bgr = np.power(enhanced_bgr / 255.0, gamma) * 255.0
    enhanced_bgr = np.uint8(enhanced_bgr)
    
    return enhanced_bgr

def detect_face(img_path):
    img = cv2.imread(img_path)
    img = enhance_low_light(img)  # Enhance low-light image before detection
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
            result = DeepFace.verify(cropped_face, image_path, model_name="ArcFace", enforce_detection=False)
            if result["verified"]:
                date_str = datetime.now().strftime("%Y-%m-%d")
                cursor.execute("INSERT OR IGNORE INTO attendance (student_id, date, status) VALUES (?, ?, ?)",
                               (student_id, date_str, "Present"))
                conn.commit()
                conn.close()
                return f"✅ Attendance marked for {name}"
        except Exception as e:
            print(f"Error verifying face for {name}: {e}")
            continue

    conn.close()
    return "❌ Face not recognized in database"

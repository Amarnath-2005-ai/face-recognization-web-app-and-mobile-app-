from flask import Flask, render_template_string, request, jsonify
from deepface import DeepFace
from mtcnn import MTCNN
import cv2
import numpy as np
import base64
import sqlite3
from datetime import datetime
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
detector = MTCNN()

# HTML template
HTML_PAGE = '''
<h2>Face Recognition Attendance System</h2>

<video id="video" width="400" height="300" autoplay></video>
<br>
<button id="snap">Scan & Mark Attendance</button>
<p id="message"></p>

<h3>Attendance Table:</h3>
<table border="1">
<tr><th>Student ID</th><th>Name</th><th>Date</th><th>Status</th></tr>
{% for row in attendance %}
<tr>
<td>{{ row[0] }}</td><td>{{ row[1] }}</td><td>{{ row[2] }}</td><td>{{ row[3] }}</td>
</tr>
{% endfor %}
</table>

<script>
var video = document.getElementById('video');

// Access webcam
navigator.mediaDevices.getUserMedia({ video: true })
.then(stream => { video.srcObject = stream; })
.catch(err => { console.error("Error accessing webcam:", err); });

// Capture snapshot and send to server
document.getElementById('snap').addEventListener('click', function() {
    var tempCanvas = document.createElement('canvas');
    tempCanvas.width = video.videoWidth;
    tempCanvas.height = video.videoHeight;
    tempCanvas.getContext('2d').drawImage(video, 0, 0);
    var dataURL = tempCanvas.toDataURL('image/jpeg');

    fetch('/scan', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ image: dataURL })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('message').innerText = data.message;
        if(!data.message.includes("✅")) alert(data.message);
        location.reload();
    });
});
</script>
'''

# Helper: detect face and return cropped face path
def detect_face(img_path):
    img = cv2.imread(img_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    faces = detector.detect_faces(img_rgb)
    if faces:
        x, y, w, h = faces[0]['box']
        face = img_rgb[y:y+h, x:x+w]
        temp_face_path = os.path.join(UPLOAD_FOLDER, "temp_face.jpg")
        face_bgr = cv2.cvtColor(face, cv2.COLOR_RGB2BGR)
        cv2.imwrite(temp_face_path, face_bgr)
        return temp_face_path
    return None

# Check face and mark attendance
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

# Routes
@app.route("/")
def home():
    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT a.student_id, s.name, a.date, a.status 
        FROM attendance a
        JOIN students s ON a.student_id = s.student_id
        ORDER BY a.date DESC
    """)
    attendance = cursor.fetchall()
    conn.close()
    return render_template_string(HTML_PAGE, attendance=attendance)

@app.route("/scan", methods=["POST"])
def scan():
    data = request.get_json()
    img_data = data['image'].split(',')[1]
    img_bytes = base64.b64decode(img_data)
    nparr = np.frombuffer(img_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    snapshot_path = os.path.join(UPLOAD_FOLDER, "snapshot.jpg")
    cv2.imwrite(snapshot_path, img)

    message = check_and_mark_attendance(snapshot_path)
    return jsonify({'message': message})

if __name__ == "__main__":
    app.run(debug=True)

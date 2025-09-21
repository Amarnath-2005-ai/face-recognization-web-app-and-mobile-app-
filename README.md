# Face Detection Based Attendance System

A web-based attendance system that uses face recognition technology to automatically mark student attendance. The system captures live video from the user's webcam, detects faces, and matches them against a database of registered students to mark attendance.

## Features

- **Real-time Face Detection**: Uses webcam to capture live video feed
- **Face Recognition**: Employs DeepFace with Facenet model for accurate face matching
- **Web Interface**: Clean and simple web interface for attendance marking
- **Database Management**: SQLite database to store student information and attendance records
- **Student Management**: Add new students to the system with their photos
- **Attendance Tracking**: View attendance records with date and status information

## Technology Stack

- **Backend**: Flask (Python web framework)
- **Face Detection**: MTCNN (Multi-task CNN)
- **Face Recognition**: DeepFace with Facenet model
- **Computer Vision**: OpenCV
- **Database**: SQLite
- **Frontend**: HTML, JavaScript (with webcam API)

## Prerequisites

Before running the application, make sure you have the following installed:

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. **Clone or download the project** to your local machine

2. **Install required Python packages**:
   ```bash
   pip install flask deepface mtcnn opencv-python numpy
   ```

3. **Set up the database**:
   ```bash
   python database_setup.py
   ```

4. **Add students to the system** (optional):
   ```bash
   python add_student.py
   ```

## Usage

1. **Start the application**:
   ```bash
   python app.py
   ```

2. **Open your web browser** and navigate to:
   ```
   http://localhost:5000
   ```

3. **Allow camera access** when prompted by your browser

4. **Mark attendance**:
   - Click the "Scan & Mark Attendance" button
   - The system will capture a snapshot and attempt to recognize the face
   - If a match is found, attendance will be marked automatically
   - If no match is found, an error message will be displayed

## Project Structure

```
face detection based attendence system/
├── app.py                 # Main Flask application
├── database_setup.py      # Database initialization script
├── add_student.py         # Script to add new students
├── face_detection.py      # Face detection utilities
├── attendance_check.py    # Attendance checking functions
├── clear_attendance.py    # Script to clear attendance records
├── attendance.db          # SQLite database file
├── faces_db/             # Directory containing student face images
│   ├── a.jpg
│   ├── b.jpg
│   └── d.jpg
├── uploads/              # Directory for temporary uploaded images
│   ├── snapshot.jpg
│   └── temp_face.jpg
├── .gitignore           # Git ignore file
└── README.md            # This file
```

## Database Schema

### Students Table
- `student_id` (TEXT, PRIMARY KEY): Unique identifier for each student
- `name` (TEXT): Student's name
- `image_path` (TEXT): Path to the student's face image

### Attendance Table
- `student_id` (TEXT): Foreign key referencing students table
- `date` (TEXT): Date of attendance (YYYY-MM-DD format)
- `status` (TEXT): Attendance status (e.g., "Present")
- Primary Key: (student_id, date)

## Adding Students

To add new students to the system:

1. Place the student's face image in the `faces_db/` directory
2. Run the `add_student.py` script:
   ```bash
   python add_student.py
   ```
3. Follow the prompts to enter student ID, name, and image filename

## Troubleshooting

### Common Issues

1. **Camera not working**: Ensure your browser has permission to access the camera
2. **Face not detected**: Make sure there's good lighting and the face is clearly visible
3. **Recognition fails**: Ensure the face image in the database is clear and well-lit
4. **Module not found errors**: Make sure all required packages are installed

### Performance Tips

- Ensure good lighting conditions for better face detection
- Use clear, high-quality images for student registration
- Keep the camera at an appropriate distance from the face

## Security Considerations

- This system is designed for educational/demonstration purposes
- For production use, consider implementing proper authentication and security measures
- Ensure student data privacy and compliance with relevant regulations

## Future Enhancements

- User authentication and role-based access
- Export attendance reports to CSV/Excel
- Email notifications for attendance marking
- Mobile-responsive design
- Batch student registration
- Attendance analytics and reporting

## License

This project is open source and available under the MIT License.

## Contributing

Feel free to contribute to this project by:
- Reporting bugs
- Suggesting new features
- Submitting pull requests
- Improving documentation

## Support

If you encounter any issues or have questions, please create an issue in the project repository or contact the development team.

---

## Made with ❤️ by Amarnath

---

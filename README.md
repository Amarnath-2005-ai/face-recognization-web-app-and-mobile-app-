# Face Detection Based Attendance System

A web-based attendance system that uses face recognition technology to automatically mark student attendance. The system captures live video from the user's webcam, detects faces, and matches them against a database of registered students to mark attendance.

## Features

- **Real-time Face Detection**: Uses webcam to capture live video feed with MTCNN
- **Advanced Face Recognition**: Employs DeepFace with ArcFace model for high accuracy and excellent dim lighting performance
- **Low-Light Optimization**: Enhanced image preprocessing for better recognition in dim lighting conditions
- **Web Interface**: Clean and simple web interface for attendance marking
- **Database Management**: SQLite database to store student information and attendance records
- **Student Management**: Easy addition of new students with their photos
- **Attendance Tracking**: View attendance records with date and status information
- **Fast Processing**: Optimized for small groups with quick recognition

## Technology Stack

- **Backend**: Flask (Python web framework)
- **Face Detection**: MTCNN (Multi-task CNN) - lightweight and accurate
- **Face Recognition**: DeepFace with ArcFace model - optimized for dim lighting
- **Computer Vision**: OpenCV with advanced image preprocessing
- **Image Enhancement**: LAB color space processing with CLAHE and gamma correction
- **Database**: SQLite - lightweight and efficient
- **Frontend**: HTML, JavaScript (with webcam API)

## Prerequisites

Before running the application, make sure you have the following installed:

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. **Clone or download the project** to your local machine

2. **Install required Python packages**:
   ```bash
   pip install -r requirements.txt
   ```
   
   **Having TensorFlow installation issues?** 
   - Check `INSTALLATION_GUIDE.md` for detailed troubleshooting
   - Try: `pip install tensorflow-cpu` if standard installation fails
   - Alternative: Use `requirements-light.txt` for lighter installation

3. **Set up the database**:
   ```bash
   python database_setup.py
   ```

4. **Add students to the system**:
   ```bash
   python add_student.py
   ```
   This will add 3 sample students. You can modify the `add_student.py` file to add your own students.

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


### **Adding New Students**
To add new students to the system:

1. **Place the student's face image** in the `faces_db/` directory
2. **Edit the `add_student.py` file** to add your student:
   ```python
   add_student("student_id", "Student Name", "faces_db/photo.jpg")
   ```
3. **Run the script**:
   ```bash
   python add_student.py
   ```

### **Photo Requirements**
- **Format**: JPG, PNG, or other common image formats
- **Quality**: Clear, well-lit, front-facing photo
- **Size**: At least 200x200 pixels recommended
- **Lighting**: Works well in dim lighting with enhanced preprocessing

## Troubleshooting

### Common Issues

1. **Camera not working**: Ensure your browser has permission to access the camera
2. **Face not detected**: The system now works well in dim lighting, but ensure the face is clearly visible
3. **Recognition fails**: 
   - Ensure the face image in the database is clear and well-lit
   - Check that the student's face is facing the camera directly
   - Try adjusting the lighting or camera position
4. **Module not found errors**: Make sure all required packages are installed using `pip install -r requirements.txt`
5. **ArcFace model loading slowly**: First-time model loading may take a few minutes - this is normal

### Performance Tips

- **Lighting**: The system works well in dim lighting, but good lighting still improves accuracy
- **Image Quality**: Use clear, high-quality images for student registration
- **Camera Position**: Keep the camera at an appropriate distance (1-2 feet) from the face
- **Face Angle**: Ensure the face is facing the camera directly for best results
- **Small Groups**: This system is optimized for small groups (3-10 students) for best performance

## Security Considerations

- This system is designed for educational/demonstration purposes
- For production use, consider implementing proper authentication and security measures
- Ensure student data privacy and compliance with relevant regulations

## System Specifications

### **Current Setup**
- **Students**: 3 students with 1 photo each
- **Recognition Model**: ArcFace (optimized for dim lighting)
- **Processing Speed**: Very fast (3 comparisons per scan)
- **Accuracy**: High with good quality photos
- **Lighting**: Works well in dim lighting conditions

### **Recommended Use Cases**
- Small classrooms (3-10 students)
- Lab sessions and workshops
- Small group meetings
- Family attendance tracking
- Prototype and demo systems

## Future Enhancements

- User authentication and role-based access
- Export attendance reports to CSV/Excel
- Email notifications for attendance marking
- Mobile-responsive design
- Batch student registration
- Attendance analytics and reporting
- Multiple photo support per student
- Real-time attendance dashboard

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

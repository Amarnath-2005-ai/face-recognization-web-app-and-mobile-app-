## Platform-Specific Notes

### Windows

The application should work out of the box on Windows. If you encounter any issues:

1. Ensure you have the latest Visual C++ Redistributable installed
2. Use a Python version between 3.8 and 3.11
3. If webcam issues occur, try running as administrator
4. For CUDA support (optional), install NVIDIA CUDA Toolkit and cuDNN

### Linux

Additional system packages may be required:

```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install -y \
    python3-dev \
    python3-pip \
    python3-venv \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev

# Fedora
sudo dnf install -y \
    python3-devel \
    mesa-libGL \
    libglib2.0-0 \
    libSM \
    libXext \
    libXrender

# Arch Linux
sudo pacman -S \
    python-pip \
    mesa \
    glib2 \
    libsm \
    libxext \
    libxrender
```

### macOS

1. Install Xcode Command Line Tools:
   ```bash
   xcode-select --install
   ```

2. For M1/M2 Macs:
   - Use tensorflow-macos instead of regular tensorflow
   - Some packages might need Rosetta 2:
     ```bash
     softwareupdate --install-rosetta
     ```

3. Using Homebrew (recommended):
   ```bash
   brew install python3
   brew install cmake  # Required for some dependencies
   ```

### Server Deployment

For server deployment (e.g., AWS, GCP, Azure):

1. Use requirements-minimal.txt for lighter installation
2. Consider using opencv-python-headless instead of opencv-python
3. Use tensorflow-cpu to avoid GPU dependencies
4. Set Flask server:
   ```python
   if __name__ == '__main__':
       app.run(host='0.0.0.0', port=5000)
   ```

### Docker Support

If you prefer using Docker, a Dockerfile is provided:

```dockerfile
FROM python:3.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python packages
COPY requirements-minimal.txt .
RUN pip install --no-cache-dir -r requirements-minimal.txt

# Copy application files
COPY . .

# Run the application
CMD ["python", "app.py"]
```

Build and run:
```bash
docker build -t face-attendance .
docker run -p 5000:5000 face-attendance
```
# Drowsi - Driver Drowsiness Detection System

## Overview
Drowsi is an intelligent driver drowsiness detection system that uses computer vision and machine learning to monitor driver alertness in real-time. The system combines multiple detection methods including eye tracking, head pose estimation, and facial landmarks analysis to provide accurate drowsiness detection.

## Key Features

### 1. Real-time Drowsiness Detection
- **Eye Aspect Ratio (EAR) Analysis**: Monitors eye closure patterns
- **Mouth Aspect Ratio (MAR) Analysis**: Detects yawning
- **Head Pose Estimation**: Tracks head position and movement
- **Blink Rate Monitoring**: Analyzes blink frequency and duration

### 2. Alert System
- **Visual Alerts**: On-screen warnings
- **Audio Alerts**: Customizable sound notifications
- **Real-time Feedback**: Immediate response to drowsiness indicators

### 3. User Management
- **Secure Authentication**: User registration and login
- **Profile Management**: User profile customization
- **Session Tracking**: Monitor and store user sessions
- **OTP Verification**: Email-based verification system

## Technical Stack

### Backend
- **Python 3.9.9**
- **Flask**: Web framework
- **OpenCV**: Computer vision processing
- **MediaPipe**: Face mesh detection
- **YOLO**: Object detection
- **MongoDB**: Database management
- **Flask-SocketIO**: Real-time communication

### Computer Vision
- **Face Recognition**: Facial landmark detection
- **Head Pose Estimation**: 3D head position tracking
- **Eye Tracking**: Blink detection and analysis
- **Yawn Detection**: Mouth movement analysis

## Installation

### Prerequisites
- Python 3.9.9
- Webcam
- MongoDB Atlas account
- Internet connection

### Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/lokeshpanthangi/drowsi.git
   cd drowsi
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure MongoDB**
   - Create a MongoDB Atlas account
   - Update the connection string in `app.py`
   - Create a database named "Drowsi"

4. **Configure Email Settings**
   - Update email credentials in the `send_otp_email` function
   - Configure SMTP settings for OTP verification

## Usage

1. **Start the Application**
   ```bash
   python app.py
   ```

2. **Access the Web Interface**
   - Open your browser and navigate to: http://localhost:5000

3. **User Registration**
   - Create a new account
   - Verify email with OTP
   - Complete profile setup

4. **Drowsiness Detection**
   - Allow camera access
   - Position yourself in front of the camera
   - System will automatically start monitoring

## Detection Parameters

- **Eye Closure Threshold**: 0.25 (EAR)
- **Yawn Detection Threshold**: 0.42 (MAR)
- **Blink Duration Threshold**: 3 seconds
- **Head Pose Alert Delay**: 8 seconds
- **Yawn Alert Delay**: 5 seconds

## Safety Features

- **Adaptive Thresholds**: Adjusts to individual users
- **Multiple Detection Methods**: Reduces false positives
- **Real-time Processing**: Immediate response to drowsiness
- **User Customization**: Adjustable alert settings

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## Support
For support, email: lokeshpantangi@gmail.com

## Acknowledgments
- MediaPipe for face mesh detection
- YOLO for object detection
- OpenCV for computer vision processing
- Flask for web framework

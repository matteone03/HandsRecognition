✋ Hand Gesture Recognition (Python, OpenCV, Mediapipe)
Overview

A real-time hand gesture recognition prototype built with Python, OpenCV, and Mediapipe.
The system detects and tracks hand movements from a webcam feed and classifies basic gestures, enabling experiments in human-computer interaction (HCI).

This project was an opportunity to combine computer vision techniques with practical engineering, focusing on performance and real-time reliability.

Features

📷 Real-time video capture and processing (~30 FPS).

✋ Hand landmark detection and tracking using Mediapipe.

🔎 Basic gesture recognition (e.g., open hand, fist, pointing).

🛠 Modular design → easy to extend with new gestures or custom actions.

Technical Details

- Language: Python 3

- Libraries: OpenCV, Mediapipe, NumPy

Pipeline:

- Capture frames from webcam.

- Detect and extract hand landmarks.

- Classify gestures based on relative landmark positions.

- Performance: Optimised frame processing to maintain ~30 FPS.

# Clone the repository
git clone https://github.com/matteone03/hand-gesture-recognition.git
cd hand-gesture-recognition

# Install dependencies
pip install -r requirements.txt

# Run the program
python3 main.py

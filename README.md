# PBL3: ARTIFICIAL INTELLIGENCE FOR INTEGRATED SYSTEM AND APPLICATION
Use OpenCV, dlib to check for drowsiness on Raspberry Pi 4, connect with Firebase and Thunkable

Cre: https://miai.vn/2020/02/26/computer-vision-pi-chuong-3-lap-dat-pi-tren-xe-hoi-de-phat-hien-tai-xe-ngu-gat/

Download the origin trained file: https://www.mediafire.com/file/1c8qfqbs662x22j/shape_predictor_68_face_landmarks.dat/file


# Drowsiness Recognition System

## Overview
This project, developed by Nguyen Thi Tam, Tran Hoang Minh, and Le Tu Bao Khanh from the 21ECE class at The University of Science and Technology, Da Nang, focuses on a **Drowsiness Recognition System** to enhance road safety by detecting driver fatigue. The system uses AI-based facial landmark detection to identify signs of drowsiness and alert drivers, integrated with a mobile application for real-time notifications. The project was mentored by Associate Professor Dr. Pham Van Tuan and teaching assistant Mr. Ho Xuan Dat, completed on June 14, 2024.

Here's the quick demo
![Bản sao của Group4_Demo (1)](https://github.com/user-attachments/assets/ea13ed13-ee64-4535-8e93-71080ba35b3e)


## Table of Contents
- [Project Description](#project-description)
- [System Design](#system-design)
- [Methodology](#methodology)
- [Experiment Setup](#experiment-setup)
- [Mobile Application](#mobile-application)
- [Results](#results)
- [Repository Structure](#repository-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Future Work](#future-work)
- [Contributing](#contributing)
- [License](#license)

## Project Description
The Drowsiness Recognition System aims to prevent road accidents caused by driver fatigue, a significant issue contributing to economic losses of VND 40,000–60,000 billion annually in Vietnam and approximately 2.9% of the country's GDP. The system leverages AI to detect drowsiness through facial landmarks, specifically focusing on eye behavior using the Eye Aspect Ratio (EAR). It integrates with the vehicle’s audio system to issue alerts and uses a mobile app for notifications to the driver’s family via WhatsApp.

## System Design
The system is built around a **Raspberry Pi 4 Model B** and includes:
- **Rapoo C200 USB Webcam** for capturing video input.
- **PC Speaker** (or vehicle AUX port) for audio alerts.
- **Cloud Integration** with Firebase for real-time data storage and Thunkable for the mobile app interface.
- **Functionality**:
  - Detects faces using Histogram of Oriented Gradients (HOG) and Support Vector Machine (SVM).
  - Identifies 68 facial landmarks with Dlib to calculate EAR for drowsiness detection.
  - Sends alerts via audio and WhatsApp notifications through the CallMeBot API.

![WiringDiagram](https://github.com/hminh1012/PBL3_DrowsinessDetection/blob/288083382c73c41a1a22481f7c49733fdec4c7a4/img/WiringDiagram.png)

Key features:
- **Real-Time Detection**: Monitors eye closure and head movements.
- **Alerts**: Triggers audio alerts and WhatsApp messages when drowsiness is detected.
- **Data Logging**: Stores detection data for analysis via Firebase.
- **User-Friendly**: Adjustable alarm settings, compact design, and affordable (under $2 million VND).

## Methodology
The system employs the **Design Thinking** process (Empathize, Define, Ideate, Prototype, Test) to address drowsy driving. The core algorithm uses:
- **Haar Cascade** and **HOG + SVM** for face detection.
- **Dlib’s Facial Landmark Detection** to identify 68 facial points, focusing on eyes.
- **Eye Aspect Ratio (EAR)** to measure eye closure duration, as introduced by Soukupova and Cech (2016).
- **AdaBoost** for combining weak classifiers to improve detection accuracy.
- **iBUG 300-W Dataset** for training the facial landmark predictor.

The system processes video frames, calculates EAR, and triggers alerts if drowsiness indicators (e.g., prolonged eye closure) are detected.

## Experiment Setup
The hardware setup includes:
- **Raspberry Pi 4 Model B** (cost: 1,590,000 VND).
- **Rapoo C200 USB Webcam** for video capture.
- **PC Speaker** or vehicle audio system for alerts.

![setup](https://github.com/hminh1012/PBL3_DrowsinessDetection/blob/288083382c73c41a1a22481f7c49733fdec4c7a4/img/Setup.png)

Software stack:
- **Python** for system development.
- **OpenCV** for image processing and Haar Cascade face detection.
- **Dlib** for facial landmark detection.
- **Imutils, NumPy** for utility functions and numerical operations.
- **Firebase** for real-time database storage.
- **Thunkable** for mobile app development.
- **CallMeBot API** for WhatsApp notifications.

Testing was conducted across various conditions (e.g., day/night, straight/tilted face angles, with/without glasses) in both lab and in-car environments, using a dataset of images and videos.

## Mobile Application
The **Thunkable-based mobile app** provides:
- **Real-Time Notifications**: Alerts via Firebase when drowsiness is detected.
- **WhatsApp Integration**: Sends messages to family members using CallMeBot API.
- **User Interface**: Displays system status and allows configuration of alerts.

The app connects to the Firebase real-time database (e.g., `https://pidrowsiness-277a4-default-rtdb.firebaseio.com`) for seamless data access.

![app](https://github.com/hminh1012/PBL3_DrowsinessDetection/blob/288083382c73c41a1a22481f7c49733fdec4c7a4/img/PhoneApp.png)

## Results
The system achieved high accuracy in controlled environments, with slightly reduced performance in low-light conditions (e.g., nighttime with streetlights). Key findings:
- **Lab Testing**: High accuracy for straight and tilted face angles.
- **In-Car Testing**: Effective during daytime; lower accuracy at night without interior lighting.
- **Glasses Impact**: Minimal effect on detection, but sunglasses prevent eye detection.
- **Evaluation Metrics**: Detailed in Tables 12–14, covering eye state recognition under various conditions.

![result](https://github.com/hminh1012/PBL3_DrowsinessDetection/blob/288083382c73c41a1a22481f7c49733fdec4c7a4/img/Drowsiness_demo.png)

## Repository Structure (on-going)
```
Drowsiness-Recognition/
├── src/
│   ├── alarm.wav                               # Audio alert system
│   ├── haarcascade_frontalface_default.xml     # HaarCascade facial detection
   
│   ├── main.py                                 # Main file
│   ├── shape_predictor_68_face_landmarks.dat   # Dlib facial landmark detection
     

├── docs/
│   ├── Report_PBL3_Team_4.pdf   # Project documentation
├── README.md                    # Project overview and instructions
```

## Requirements
- **Hardware**:
  - Raspberry Pi 4 Model B
  - Rapoo C200 USB Webcam
  - PC Speaker or vehicle AUX port
- **Software**:
  - Python 3.x
  - OpenCV, Dlib, Imutils, NumPy
  - Firebase SDK
  - Thunkable for mobile app
  - CallMeBot API for WhatsApp integration
- **Dependencies**:
  - Install Python libraries (optional): `pip install opencv-python dlib imutils numpy firebase-admin` 

## Installation (on-going)
1. Clone the repository:
   ```bash
    https://github.com/hminh1012/PBL3_DrowsinessDetection.git
   ```
2. Set up the Raspberry Pi 4 with the webcam and speaker.
3. Install dependencies:
   ```bash
   pip install -r setup.txt
   ```

4. Set up the Thunkable app and CallMeBot API for notifications.
5. Deploy the mobile app on a compatible device (iOS/Android).

## Usage
1. Connect and power on the Raspberry Pi with the webcam and speaker.
2. Run the main script:
   ```bash
   python main.py
   ```
3. Monitor real-time detection via the Thunkable app.
4. Test the alert system by simulating drowsiness (e.g., closing eyes for a prolonged period).
5. Check Firebase for data logs and WhatsApp for notifications.

## Future Work
- Improve robustness in low-light conditions and with sunglasses.
- Develop a more intuitive user interface for system configuration.
- Implement a tracking data system for long-term driver behavior analysis.
- Optimize power consumption for prolonged operation.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue to discuss improvements or bug fixes.

## License
This project is licensed under the MIT License.

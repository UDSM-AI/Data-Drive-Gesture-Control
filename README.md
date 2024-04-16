# Data Drive

**Introduction:**
Data Drive is an innovative project aimed at exploring and developing various methods for controlling unmanned and autonomous vehicles. With a focus on user-centric interfaces and advanced control systems, Data Drive seeks to revolutionize the way we interact with and manage autonomous vehicles.

**Objective:**
The primary objective of the Data Drive project is to research and implement intuitive and efficient control interfaces for unmanned and autonomous vehicles. By leveraging cutting-edge technologies and open datasets, the project aims to enhance the accessibility, adaptability, and safety of autonomous vehicle control systems.

**Initiatives:**
1. **Gesture Control:** One of the key initiatives of the Data Drive project is Gesture Control. Through this initiative, the project explores the use of hand gestures as a means of controlling unmanned vehicles. By analyzing hand movements and gestures, the project aims to develop intuitive and responsive control interfaces that enable users to navigate vehicles effortlessly.

2. **Voice Control:** Another important initiative is Voice Control. This initiative focuses on developing natural language processing (NLP) systems that allow users to control autonomous vehicles using voice commands. By leveraging speech recognition technology and open datasets, the project aims to create a seamless and intuitive experience for users, enabling them to interact with vehicles using verbal instructions.

**Data Collection:**
To support its initiatives, Data Drive conducts extensive data collection campaigns. These campaigns involve collecting diverse and comprehensive datasets of hand gestures and voice commands from participants. The collected data serves as the foundation for developing and refining control interfaces, ensuring their accuracy, reliability, and adaptability in real-world scenarios.

**Impact:**
The Data Drive project has the potential to have a significant impact on various industries and sectors, including transportation, logistics, and robotics. By developing advanced control interfaces for unmanned and autonomous vehicles, the project aims to improve efficiency, safety, and accessibility, ultimately accelerating the adoption and integration of autonomous technologies.

# DATA DRIVE: Hand Gesture Vehicle Control

## Overview

This Python script utilizes the MediaPipe library and OpenCV to detect and track hand gestures in real-time from a webcam feed. It enables users to control vehicle movements through hand gestures, such as accelerating, braking, steering left, and steering right.

## Features

- Real-time hand gesture detection and tracking.
- Support for multiple hand gestures for controlling vehicle movements.
- Customizable actions based on detected hand positions.

## Requirements

- Python 3.x
- OpenCV (`cv2`)
- MediaPipe (`mediapipe`)
- NumPy (`numpy`)
- Custom module `src.drive_actions` (for driving actions)

## Installation

1. Install Python if not already installed: [Python Installation Guide](https://www.python.org/downloads/)
2. Install required libraries using pip:

```bash
pip install opencv-python mediapipe numpy
```

3. Ensure the custom module `src.drive_actions` is available in the project directory.

## Usage

1. Run the script `hand_gesture_vehicle_control.py`.
2. Position your hands in front of the webcam.
3. Perform hand gestures to control vehicle movements:
   - **Left Hand**:
     - Touch thumb to index finger: Accelerate
     - Touch thumb to middle finger: Brake
     - Touch thumb to ring finger: Reverse
   - **Right Hand**:
     - Touch thumb to index finger: Steer Left
     - Touch thumb to middle finger: Steer Right
4. Press 'q' to quit the program.

## Customization

You can customize the following aspects of the script:

- Define custom actions in the `src.drive_actions` module.
- Adjust the hand gesture detection thresholds in the code to suit different hand sizes or environmental conditions.
- Modify the regions for left and right hands to optimize hand detection.

## Credits

- **OpenCV**: Open Source Computer Vision Library
- **MediaPipe**: Google's open-source framework for cross-platform customizable ML solutions for live and streaming media
- **NumPy**: Scientific computing library for Python
- **Custom Module**: `src.drive_actions` for handling driving actions

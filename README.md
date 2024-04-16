# DATA DRIVE: Hand Gesture Recognition for Vehicle Control

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
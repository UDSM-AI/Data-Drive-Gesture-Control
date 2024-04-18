import cv2
import mediapipe as mp
import numpy as np
from src.drive_actions import perform_action, release_accelerate_keys, release_steering_keys, release_forward_keys, release_reverse_keys, release_left_keys, release_right_keys
from src.finger_actions import *

def track_hand():
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands()
    mp_drawing = mp.solutions.drawing_utils

    cap = cv2.VideoCapture(0)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    left_hand_region = (0, 0, width // 2, height)
    right_hand_region = (width // 2, 0, width // 2, height)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = hands.process(rgb_frame)

        if results.multi_hand_landmarks:
            mask = np.zeros_like(frame)
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(mask, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                                        mp_drawing.DrawingSpec(color=(255, 255, 255), thickness=2,
                                                                circle_radius=2),
                                        mp_drawing.DrawingSpec(color=(255, 255, 255), thickness=2,
                                                                circle_radius=2))

                detect_hand_action(hand_landmarks, frame, width, height)

            frame = cv2.bitwise_and(frame, mask)

        cv2.rectangle(frame, (left_hand_region[0], left_hand_region[1]),
                    (left_hand_region[0] + left_hand_region[2], left_hand_region[1] + left_hand_region[3]),
                    (255, 0, 0), 2)
        cv2.rectangle(frame, (right_hand_region[0], right_hand_region[1]),
                    (right_hand_region[0] + right_hand_region[2], right_hand_region[1] + right_hand_region[3]),
                    (255, 0, 0), 2)

        cv2.imshow('Data Drive', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def detect_hand_action(hand_landmarks, frame, width, height):
    palm_landmark = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.WRIST]
    palm_x = int(palm_landmark.x * width)
    palm_y = int(palm_landmark.y * height)

    if palm_x < width // 2:
        detect_left_hand_action(hand_landmarks, frame)
    else:
        detect_right_hand_action(hand_landmarks, frame)

def detect_left_hand_action(hand_landmarks, frame):
    if is_index_finger_touching_thumb(hand_landmarks):
        cv2.putText(frame, "Accelerate", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        print("Accelerate")
        release_reverse_keys()
        perform_action("accelerate")
    elif is_middle_finger_touching_thumb(hand_landmarks):
        cv2.putText(frame, "Brake", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        print("Brake")
        release_forward_keys()
        perform_action("brake")
    elif is_ring_finger_touching_thumb(hand_landmarks):
        cv2.putText(frame, "Reverse", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        print("Reverse")
        release_accelerate_keys()
        perform_action("reverse")
    else:
        cv2.putText(frame, "No Action Detected", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        release_accelerate_keys()

def detect_right_hand_action(hand_landmarks, frame):
    if is_index_finger_touching_thumb(hand_landmarks):
        cv2.putText(frame, "Steering Left", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        print("Steering Left")
        release_right_keys()
        perform_action("steer_left")
    elif is_middle_finger_touching_thumb(hand_landmarks):
        cv2.putText(frame, "Steering Right", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        print("Steering Right")
        release_left_keys()
        perform_action("steer_right")
    elif is_ring_finger_touching_thumb(hand_landmarks):
        cv2.putText(frame, "Neutralize", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        print("Neutralize")
        release_steering_keys()
    else:
        cv2.putText(frame, "No Action Detected", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        release_steering_keys()

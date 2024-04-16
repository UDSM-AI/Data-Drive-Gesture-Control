import cv2
import mediapipe as mp
import numpy as np
import math

def is_hand_open(hand_landmarks):
    # Calculate the distance between thumb and index finger landmarks
    thumb_tip = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.THUMB_TIP]
    index_tip = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.INDEX_FINGER_TIP]
    distance = np.sqrt((thumb_tip.x - index_tip.x) ** 2 + (thumb_tip.y - index_tip.y) ** 2)
    # Define a threshold for open hand
    threshold = 0.1  # You can adjust this threshold as needed
    return distance > threshold

def is_thumb_up(hand_landmarks):
    thumb_tip = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.THUMB_TIP]
    index_tip = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.INDEX_FINGER_TIP]
    middle_tip = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.MIDDLE_FINGER_TIP]
    ring_tip = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.RING_FINGER_TIP]
    pinky_tip = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.PINKY_TIP]

    # Calculate the distances between the thumb tip and the other fingers
    thumb_index_distance = math.sqrt((thumb_tip.x - index_tip.x) ** 2 + (thumb_tip.y - index_tip.y) ** 2)
    thumb_middle_distance = math.sqrt((thumb_tip.x - middle_tip.x) ** 2 + (thumb_tip.y - middle_tip.y) ** 2)
    thumb_ring_distance = math.sqrt((thumb_tip.x - ring_tip.x) ** 2 + (thumb_tip.y - ring_tip.y) ** 2)
    thumb_pinky_distance = math.sqrt((thumb_tip.x - pinky_tip.x) ** 2 + (thumb_tip.y - pinky_tip.y) ** 2)

    # Define a threshold for thumb divergence
    threshold = 0.05  # You can adjust this threshold as needed

    # Check if the thumb is raised (diverged) from the other fingers
    if (thumb_index_distance > threshold and
        thumb_middle_distance > threshold and
        thumb_ring_distance > threshold and
        thumb_pinky_distance > threshold):
        return True
    else:
        return False

def track_hand():
    # Initialize MediaPipe Hand module
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands()
    mp_drawing = mp.solutions.drawing_utils

    # Initialize video capture
    cap = cv2.VideoCapture(0)

    # Get the frame width and height
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Define the regions for left and right hands
    left_hand_region = (0, 0, width // 2, height)
    right_hand_region = (width // 2, 0, width // 2, height)

    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Flip the frame horizontally
        frame = cv2.flip(frame, 1)

        # Convert BGR image to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Detect hand landmarks
        results = hands.process(rgb_frame)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Draw hand landmarks on the frame
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                                           mp_drawing.DrawingSpec(color=(0,255,0), thickness=2, circle_radius=2),
                                           mp_drawing.DrawingSpec(color=(255,0,0), thickness=2, circle_radius=2))
                
                # Get the palm landmark
                palm_landmark = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST]
                # Get the coordinates of the palm landmark
                palm_x = int(palm_landmark.x * width)
                palm_y = int(palm_landmark.y * height)

                # Check if the palm is in the right hand region
                if palm_x >= width // 2:
                    # Check which finger is raised
                    for idx, finger_tip in enumerate([4, 8, 12, 16, 20]):  # Thumb, Index, Middle, Ring, Pinky
                        if idx == 0:  # Thumb
                            if is_thumb_up(hand_landmarks):
                                cv2.putText(frame, f"Right Hand: {finger_names[idx]} Finger Up", 
                                            (width // 2 + 10, 50 + idx * 50), 
                                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                                print(f"Right Hand: {finger_names[idx]} Finger Up")
                        else:
                            if hand_landmarks.landmark[finger_tip].y < hand_landmarks.landmark[finger_tip - 1].y:
                                cv2.putText(frame, f"Right Hand: {finger_names[idx]} Finger Up", 
                                            (width // 2 + 10, 50 + idx * 50), 
                                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                                print(f"Right Hand: {finger_names[idx]} Finger Up")

        # Draw the regions for left and right hands on the frame
        cv2.rectangle(frame, (left_hand_region[0], left_hand_region[1]), 
                      (left_hand_region[0] + left_hand_region[2], left_hand_region[1] + left_hand_region[3]), 
                      (255, 0, 0), 2)
        cv2.rectangle(frame, (right_hand_region[0], right_hand_region[1]), 
                      (right_hand_region[0] + right_hand_region[2], right_hand_region[1] + right_hand_region[3]), 
                      (255, 0, 0), 2)

        cv2.imshow('Hand Landmarks', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    track_hand()

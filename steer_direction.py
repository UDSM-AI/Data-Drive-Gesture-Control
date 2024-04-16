import cv2
import mediapipe as mp
import numpy as np
from drive_actions import perform_action, release_accelerate_keys, release_steering_keys, release_forward_keys, release_reverse_keys, release_left_keys, release_right_keys

def is_hand_open(hand_landmarks):
    # Calculate the distance between thumb and index finger landmarks
    thumb_tip = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.THUMB_TIP]
    index_tip = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.INDEX_FINGER_TIP]
    distance = np.sqrt((thumb_tip.x - index_tip.x) ** 2 + (thumb_tip.y - index_tip.y) ** 2)
    # Define a threshold for open hand
    threshold = 0.1
    return distance > threshold


# Function to check if the top of the index finger is touching the thumb
def is_index_finger_touching_thumb(hand_landmarks):
    thumb_tip = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.THUMB_TIP]
    index_tip = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.INDEX_FINGER_TIP]
    distance = np.sqrt((thumb_tip.x - index_tip.x) ** 2 + (thumb_tip.y - index_tip.y) ** 2)
    # Define a threshold
    threshold = 0.1
    return distance < threshold

# Function to check if the top of the middle finger is touching the thumb
def is_middle_finger_touching_thumb(hand_landmarks):
    thumb_tip = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.THUMB_TIP]
    middle_tip = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.MIDDLE_FINGER_TIP]
    distance = np.sqrt((thumb_tip.x - middle_tip.x) ** 2 + (thumb_tip.y - middle_tip.y) ** 2)
    # Define a threshold
    threshold = 0.1
    return distance < threshold

def is_ring_finger_touching_thumb(hand_landmarks):
    thumb_tip = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.THUMB_TIP]
    ring_tip = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.RING_FINGER_TIP]
    distance = np.sqrt((thumb_tip.x - ring_tip.x) ** 2 + (thumb_tip.y - ring_tip.y) ** 2)
    # Define a threshold
    threshold = 0.1
    return distance < threshold

def is_pinky_finger_touching_thumb(hand_landmarks):
    thumb_tip = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.THUMB_TIP]
    pinky_tip = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.PINKY_TIP]
    distance = np.sqrt((thumb_tip.x - pinky_tip.x) ** 2 + (thumb_tip.y - pinky_tip.y) ** 2)
    # Define a threshold
    threshold = 0.1
    return distance < threshold



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
            # Create a black mask image
            mask = np.zeros_like(frame)

            for hand_landmarks in results.multi_hand_landmarks:
                # Draw hand landmarks on the mask
                mp_drawing.draw_landmarks(mask, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                                        mp_drawing.DrawingSpec(color=(255,255,255), thickness=2, circle_radius=2),
                                        mp_drawing.DrawingSpec(color=(255,255,255), thickness=2, circle_radius=2))

                # Perform actions based on hand position
                # Get the palm landmark
                palm_landmark = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST]
                # Get the coordinates of the palm landmark
                palm_x = int(palm_landmark.x * width)
                palm_y = int(palm_landmark.y * height)
                # Check if the palm is in the left hand region
                if palm_x < width // 2:
                    # Check if the top of the index finger is touching the thumb
                    if is_index_finger_touching_thumb(hand_landmarks):
                        cv2.putText(frame, "Accelerate", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                        print("Accelerate")
                        release_reverse_keys()
                        perform_action("accelerate")
                    # Check if the top of the middle finger is touching the thumb
                    elif is_middle_finger_touching_thumb(hand_landmarks):
                        cv2.putText(frame, "Brake", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                        print("Brake")
                        release_forward_keys()
                        perform_action("brake")
                    #check if the top of the ring finger is touching the thumb
                    elif is_ring_finger_touching_thumb(hand_landmarks):
                        cv2.putText(frame, "Reverse", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                        print("Reverse")
                        release_accelerate_keys()
                        perform_action("reverse")
                    else:
                        cv2.putText(frame, "No Action Detected", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                        release_accelerate_keys()

                # Check if the palm is in the right hand region
                else:
                    cv2.putText(frame, "Right Hand", (width - 200, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    # Check if the top of the index finger is touching the thumb
                    if is_index_finger_touching_thumb(hand_landmarks):
                        cv2.putText(frame, "Steering Left", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                        print("Steering Left")
                        release_right_keys()
                        perform_action("steer_left")
                    # Check if the top of the middle finger is touching the thumb
                    elif is_middle_finger_touching_thumb(hand_landmarks):
                        cv2.putText(frame, "Steering Right", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                        print("Steering Right")
                        release_left_keys()
                        perform_action("steer_right")
                    # Check if the top of the ring finger is touching the thumb
                    elif is_ring_finger_touching_thumb(hand_landmarks):
                        cv2.putText(frame, "Neutralize", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                        print("Neutralize")
                        release_steering_keys()
                    else:
                        cv2.putText(frame, "No Action Detected", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                        release_steering_keys()


            # Overlay the mask on the original frame
            frame = cv2.bitwise_and(frame, mask)

        # Draw the regions for left and right hands on the frame
        cv2.rectangle(frame, (left_hand_region[0], left_hand_region[1]), (left_hand_region[0] + left_hand_region[2], left_hand_region[1] + left_hand_region[3]), (255, 0, 0), 2)
        cv2.rectangle(frame, (right_hand_region[0], right_hand_region[1]), (right_hand_region[0] + right_hand_region[2], right_hand_region[1] + right_hand_region[3]), (255, 0, 0), 2)

        cv2.imshow('Hand Landmarks', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    track_hand()

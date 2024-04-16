import cv2
import mediapipe as mp
import math
from drive_actions import perform_action

def calculate_angle(a, b, c):
    """Calculate angle between three points"""
    radians = math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0])
    angle = math.degrees(radians)
    angle = angle + 360 if angle < 0 else angle
    return angle

def track_hand():
    # Initialize MediaPipe Hand module
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands()
    mp_drawing = mp.solutions.drawing_utils

    # Initialize video capture
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Convert BGR image to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Detect hand landmarks
        results = hands.process(rgb_frame)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Draw hand landmarks
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Extract finger landmarks
                thumb = hand_landmarks.landmark[4]
                index = hand_landmarks.landmark[8]
                middle = hand_landmarks.landmark[12]
                ring = hand_landmarks.landmark[16]
                pinky = hand_landmarks.landmark[20]

                # Calculate angles between fingers
                thumb_angle = calculate_angle((thumb.x, thumb.y), (index.x, index.y), (middle.x, middle.y))
                index_angle = calculate_angle((index.x, index.y), (thumb.x, thumb.y), (middle.x, middle.y))
                middle_angle = calculate_angle((middle.x, middle.y), (index.x, index.y), (ring.x, ring.y))
                ring_angle = calculate_angle((ring.x, ring.y), (middle.x, middle.y), (pinky.x, pinky.y))

                # Check if thumb and index finger form a finger gun gesture
                if thumb_angle < 50 and index_angle > 130:
                    cv2.putText(frame, "Steer Right", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    # Perform action for steering right
                    perform_action("steer_right")
                elif thumb_angle > 130 and index_angle < 50:
                    cv2.putText(frame, "Steer Left", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    # Perform action for steering left
                    perform_action("steer_left")

        cv2.imshow('Hand Tracking', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    track_hand()

import cv2
import mediapipe as mp
import math
from drive_actions import perform_action


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

    # Define the regions for left, center, and right
    left_region = (0, 0, width // 3, height)
    center_region = (width // 3, 0, width // 3, height)
    right_region = (2 * width // 3, 0, width // 3, height)

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
                # Get the palm landmark
                palm_landmark = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST]

                # Get the coordinates of the palm landmark
                palm_x = int(palm_landmark.x * width)
                palm_y = int(palm_landmark.y * height)

                # Draw a circle at the palm position
                cv2.circle(frame, (palm_x, palm_y), 10, (0, 255, 0), -1)

                # Check if the palm is in the left region
                if palm_x < left_region[2]:
                    cv2.putText(frame, "Steer Left", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    # Perform action for steering left
                    # perform_action("steer_left")
                # Check if the palm is in the center region
                elif left_region[2] <= palm_x < right_region[0]:
                    cv2.putText(frame, "Relax", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    # Perform action for relaxing
                    # perform_action("relax")
                # Check if the palm is in the right region
                elif palm_x >= right_region[0]:
                    cv2.putText(frame, "Steer Right", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    # Perform action for steering right
                    # perform_action("steer_right")

        # Draw the regions on the frame
        cv2.rectangle(frame, (left_region[0], left_region[1]), (left_region[0] + left_region[2], left_region[1] + left_region[3]), (255, 0, 0), 2)
        cv2.rectangle(frame, (center_region[0], center_region[1]), (center_region[0] + center_region[2], center_region[1] + center_region[3]), (255, 0, 0), 2)
        cv2.rectangle(frame, (right_region[0], right_region[1]), (right_region[0] + right_region[2], right_region[1] + right_region[3]), (255, 0, 0), 2)

        cv2.imshow('Hand Tracking', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    track_hand()

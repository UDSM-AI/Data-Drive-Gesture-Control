import cv2
import mediapipe as mp
import ctypes

def get_screen_resolution():
    user32 = ctypes.windll.user32
    width, height = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    return width, height

def track_hand_landmarks(frame, hand_tracking):
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hand_tracking.process(rgb_frame)
    landmarks = []
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            hand_landmark_list = []
            for landmark in hand_landmarks.landmark:
                ih, iw, _ = frame.shape
                cx, cy = int(landmark.x * iw), int(landmark.y * ih)
                hand_landmark_list.append((cx, cy))
                cv2.circle(frame, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
            landmarks.append(hand_landmark_list)
    return frame, landmarks

def main():
    # Initialize MediaPipe Hand Tracking module
    hand_tracking = mp.solutions.hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)

    # Get screen resolution
    screen_width, screen_height = get_screen_resolution()

    # Initialize VideoCapture
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Resize frame to match screen resolution
        frame = cv2.resize(frame, (screen_width, screen_height))

        # Mirror the frame horizontally
        frame = cv2.flip(frame, 1)

        # Track hand landmarks
        frame, hand_landmarks = track_hand_landmarks(frame, hand_tracking)

        # Perform gesture recognition
        if hand_landmarks:
            # Example: Detect pointing left
            index_finger_tip = hand_landmarks[0][8]  # Assuming only one hand
            # Define a region of interest for pointing left
            # Adjust the threshold and region coordinates as needed
            if index_finger_tip[0] < 200:
                cv2.putText(frame, 'Pointing Left', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

        # Display output
        cv2.imshow('Hand Gesture Recognition', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release VideoCapture and close all windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

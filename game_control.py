import cv2
import mediapipe as mp
import ctypes
import keyboard

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

def map_gestures_to_keys(hand_landmarks):
    # Assuming only one hand is present
    if hand_landmarks:
        fingers = [hand_landmarks[0][4], hand_landmarks[0][8], hand_landmarks[0][12], hand_landmarks[0][16], hand_landmarks[0][20]]
        thumb, index, middle, ring, little = fingers

        # Check pointing left
        if index[0] < thumb[0]:
            keyboard.press('a')
            keyboard.release('a')

        # Check pointing right
        elif index[0] > thumb[0]:
            keyboard.press('d')
            keyboard.release('d')

        # Check clenched fist
        if all(finger[1] < thumb[1] for finger in fingers):
            keyboard.press('space')
            keyboard.release('space')

        # Check raised palm
        elif all(finger[1] > thumb[1] for finger in fingers):
            keyboard.press('w')
            keyboard.release('w')

        # Check spread fingers
        elif all(finger[0] < thumb[0] for finger in fingers):
            keyboard.press('s')
            keyboard.release('s')

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

        # Mirror the frame horizontally
        frame = cv2.flip(frame, 1)

        # Resize frame to match screen resolution
        frame = cv2.resize(frame, (screen_width, screen_height))

        # Track hand landmarks
        frame, hand_landmarks = track_hand_landmarks(frame, hand_tracking)

        # Map hand gestures to keyboard keys
        map_gestures_to_keys(hand_landmarks)

        # Display output
        cv2.imshow('Hand Gesture Recognition', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release VideoCapture and close all windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

import cv2
import mediapipe as mp
import ctypes

def get_screen_resolution():
    user32 = ctypes.windll.user32
    width, height = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    return width, height

def track_pose_landmarks(frame, pose_detection):
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose_detection.process(rgb_frame)
    if results.pose_landmarks:
        for landmark in results.pose_landmarks.landmark:
            ih, iw, _ = frame.shape
            cx, cy = int(landmark.x * iw), int(landmark.y * ih)
            cv2.circle(frame, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
    return frame

def main():
    # Initialize MediaPipe Pose Detection module
    pose_detection = mp.solutions.pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)

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

        # Track pose landmarks
        frame = track_pose_landmarks(frame, pose_detection)

        # Display output
        cv2.imshow('Full Body Pose Estimation', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release VideoCapture and close all windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

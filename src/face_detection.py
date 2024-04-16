import cv2
import mediapipe as mp

# Function to perform face detection
def detect_faces(frame, face_detection):
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_detection.process(rgb_frame)
    if results.detections:
        for detection in results.detections:
            bboxC = detection.location_data.relative_bounding_box
            ih, iw, _ = frame.shape
            x, y, w, h = int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    return frame

# Function to perform hand tracking
def track_hands(frame, hand_tracking):
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hand_tracking.process(rgb_frame)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            for landmark in hand_landmarks.landmark:
                ih, iw, _ = frame.shape
                cx, cy = int(landmark.x * iw), int(landmark.y * ih)
                cv2.circle(frame, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
    return frame

def main():
    # Initialize MediaPipe Face Detection and Hand Tracking modules
    face_detection = mp.solutions.face_detection.FaceDetection(min_detection_confidence=0.5)
    hand_tracking = mp.solutions.hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)

    # Initialize VideoCapture
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Detect faces
        frame = detect_faces(frame, face_detection)

        # Track hands
        frame = track_hands(frame, hand_tracking)

        # Display output
        cv2.imshow('Face Detection and Hand Tracking', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release VideoCapture and close all windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

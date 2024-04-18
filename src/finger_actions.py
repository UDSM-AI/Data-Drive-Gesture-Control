from typing import Any
import numpy as np
import mediapipe as mp

def is_hand_open(hand_landmarks: Any) -> bool:
    """
    Determines if the hand is open based on the distance between thumb and index finger landmarks.

    Args:
        hand_landmarks: An object containing hand landmarks detected by MediaPipe.

    Returns:
        A boolean indicating whether the hand is open (True) or not (False).
    """
    thumb_tip = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.THUMB_TIP]
    index_tip = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.INDEX_FINGER_TIP]
    distance = np.sqrt((thumb_tip.x - index_tip.x) ** 2 + (thumb_tip.y - index_tip.y) ** 2)
    threshold = 0.1
    return distance > threshold


def is_index_finger_touching_thumb(hand_landmarks: Any) -> bool:
    """
    Checks if the top of the index finger is touching the thumb.

    Args:
        hand_landmarks: An object containing hand landmarks detected by MediaPipe.

    Returns:
        A boolean indicating whether the index finger is touching the thumb (True) or not (False).
    """
    thumb_tip = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.THUMB_TIP]
    index_tip = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.INDEX_FINGER_TIP]
    distance = np.sqrt((thumb_tip.x - index_tip.x) ** 2 + (thumb_tip.y - index_tip.y) ** 2)
    threshold = 0.1
    return distance < threshold


def is_middle_finger_touching_thumb(hand_landmarks: Any) -> bool:
    """
    Checks if the top of the middle finger is touching the thumb.

    Args:
        hand_landmarks: An object containing hand landmarks detected by MediaPipe.

    Returns:
        A boolean indicating whether the middle finger is touching the thumb (True) or not (False).
    """
    thumb_tip = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.THUMB_TIP]
    middle_tip = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.MIDDLE_FINGER_TIP]
    distance = np.sqrt((thumb_tip.x - middle_tip.x) ** 2 + (thumb_tip.y - middle_tip.y) ** 2)
    threshold = 0.1
    return distance < threshold


def is_ring_finger_touching_thumb(hand_landmarks: Any) -> bool:
    """
    Checks if the top of the ring finger is touching the thumb.

    Args:
        hand_landmarks: An object containing hand landmarks detected by MediaPipe.

    Returns:
        A boolean indicating whether the ring finger is touching the thumb (True) or not (False).
    """
    thumb_tip = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.THUMB_TIP]
    ring_tip = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.RING_FINGER_TIP]
    distance = np.sqrt((thumb_tip.x - ring_tip.x) ** 2 + (thumb_tip.y - ring_tip.y) ** 2)
    threshold = 0.1
    return distance < threshold


def is_pinky_finger_touching_thumb(hand_landmarks: Any) -> bool:
    """
    Checks if the top of the pinky finger is touching the thumb.

    Args:
        hand_landmarks: An object containing hand landmarks detected by MediaPipe.

    Returns:
        A boolean indicating whether the pinky finger is touching the thumb (True) or not (False).
    """
    thumb_tip = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.THUMB_TIP]
    pinky_tip = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.PINKY_TIP]
    distance = np.sqrt((thumb_tip.x - pinky_tip.x) ** 2 + (thumb_tip.y - pinky_tip.y) ** 2)
    threshold = 0.1
    return distance < threshold

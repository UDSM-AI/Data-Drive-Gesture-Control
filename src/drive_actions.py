import keyboard
import time

import keyboard

def perform_action(action):
    _driving_actions = {
        "accelerate": "w",
        "brake": "Space",
        "reverse": "s",
        "steer_left": "a",
        "steer_right": "d",
        "handbrake": "Space",
        "reset": "r"
    }

    try:
        key = _driving_actions.get(action)
        if key is not None:
            keyboard.press(key)
            time.sleep(.2)
            keyboard.release(key)
        else:
            print("Unknown action")
    except Exception as e:
        print(f"An error occurred: {e}")


def release_accelerate_keys():
    try:
        keyboard.release("w")
        keyboard.release("s")
    except Exception as e:
        print(f"An error occurred: {e}")


def release_steering_keys():
    try:
        keyboard.release("a")
        keyboard.release("d")
    except Exception as e:
        print(f"An error occurred: {e}")


def release_forward_keys():
    try:
        keyboard.release("w")
    except Exception as e:
        print(f"An error occurred: {e}")

def release_reverse_keys():
    try:
        keyboard.release("s")
    except Exception as e:
        print(f"An error occurred: {e}")


def release_left_keys():
    try:
        keyboard.release("a")
    except Exception as e:
        print(f"An error occurred: {e}")

def release_right_keys():
    try:
        keyboard.release("d")
    except Exception as e:
        print(f"An error occurred: {e}")


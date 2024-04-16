import keyboard
import time

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

    # key = _driving_actions.get(action)
    # if key is not None:
    #     keyboard.press(key)
    #     time.sleep(0.2)
    #     keyboard.release(key)
    # else:
    #     print("Unknown action")

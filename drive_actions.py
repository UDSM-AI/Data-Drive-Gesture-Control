import keyboard
import time

def perform_action(action):
    _driving_actions = {
        "accelerate": "W",
        "brake": "Space",
        "reverse": "S",
        "steer_left": "A",
        "steer_right": "D",
        "handbrake": "Space",
        "reset": "R"
    }

    key = _driving_actions.get(action)
    if key is not None:
        keyboard.press(key)
        # Optionally, you can add a small delay to simulate key press duration
        time.sleep(0.2)
        # Release the key after a short delay
        keyboard.release(key)
    else:
        print("Unknown action")

'''
    keyboard_utils.py

    contains keyboard related utility functions
'''

import keyboard
from keyboard import KeyboardEvent

def check_key_event(key_event: KeyboardEvent, target_key: str):
        return key_event.event_type == keyboard.KEY_DOWN and key_event.name == target_key
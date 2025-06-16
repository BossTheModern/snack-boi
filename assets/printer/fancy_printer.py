# Fancy printer to print text strings in a writing motion
import keyboard
import time
from keyboard import KeyboardEvent

class FancyPrinter:
    def __init__(self, interval: float = 0.03, pause_marker: str = '\n', line_interval: float = 1.0) -> None:
        self._interval: float = interval
        self._pause_marker: str = pause_marker
        self._line_interval: float = line_interval
    
    def print_text(self, text: str) -> None:
        '''
            Prints text where there will be an automatic delay when the printer
            meets a pause marker. It allows for user prompt after everything
            is printed
        '''
        key_event: KeyboardEvent

        for t in text:
            if t == self._pause_marker:
                time.sleep(self._line_interval)
            
            print(t, end='')
            time.sleep(self._interval)
        
        while True:
            key_event = keyboard.read_event(suppress=True)
            if key_event.event_type == keyboard.KEY_DOWN: break
        
        print()

    def print_text_line(self, text: str) -> None:
        '''
            Prints text where upon meeting a pause marker, prompts the user
            to press any button to print the next line
        '''
        key_event: KeyboardEvent

        for t in text:
            while t == self._pause_marker:
                key_event = keyboard.read_event(suppress=True)
                if key_event.event_type == keyboard.KEY_DOWN: break
            
            print(t, end='')
            time.sleep(self._interval)
'''
    account.py

    Class for handling account logic
'''

import keyboard
from keyboard import KeyboardEvent
from utils import keyboard_utils

class Account:
    _name: str
    _points: int = 0

    def show_account(self) -> None:
        '''
            Shows account
        '''
        max_width: int = len("points") + 5

        print(f"{"[ACCOUNT]":-^40}")
        print(f"{'Name:':<{max_width}} {self._name}")
        print(f"{'Points:':<{max_width}} {self._points}")
        print("[E] change name")
        print("[Q] back to main menu")
    
    def change_name(self) -> None:
        '''
            Handles logic of changing account name
        '''
        pass
    
    def account_menu(self) -> None:
        '''
            Handles account display logic
        '''

        show_menu: bool = True

        while True:
            if show_menu:
                self.show_account()
                show_menu = False
            
            key_event: KeyboardEvent = keyboard.read_event(suppress=True)

            if keyboard_utils.check_key_event(key_event, 'b'):
                print("Changing name...")

            if keyboard_utils.check_key_event(key_event, 'q'):
                print("Returning to main menu...")
                break

            show_menu = True
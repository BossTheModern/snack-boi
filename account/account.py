'''
    account.py

    Class for handling account logic
'''

import keyboard
from keyboard import KeyboardEvent
from utils import keyboard_utils
from typing import List
from assets.shop.shop_items import ShopItems
from assets.shop.shop_item import ShopItem
from assets.enums.enums import Confirmation, AccountOptions
from utils.consts import NAME_MIN_LENGTH
from utils.consts import NAME_MAX_LENGTH


class Account:
    _name: str = ""
    _points_balance: int = 100
    _owned_shop_items: List[ShopItem] = []

    def show_account(self) -> None:
        '''
            Shows account
        '''
        max_width: int = len("points") + 5

        print(f"{"[ACCOUNT]":-^40}")
        print(f"{'Name:':<{max_width}} {self._name}")
        print(f"{'Points:':<{max_width}} {self._points_balance}")

        self.show_owned_powerups()
        print(f"{'':-<40}")
        print("[E] change name")
        print("[Q] back to main menu")
    
    def show_owned_powerups(self) -> None:
        print("Owned powerups: ")
        
        if len(self._owned_shop_items) == 0:
            print("None")
        else: 
            for item in self._owned_shop_items:
                if item._stock > 0:
                    print(f"{item._name}: {item._stock:<10}")
        
    
    def account_display(self) -> None:
        '''
            Handles account display logic
        '''
        show_menu: bool = True

        while True:
            if show_menu:
                self.show_account()
                show_menu = False
            
            key_event: KeyboardEvent = keyboard.read_event(suppress=True)

            if keyboard_utils.check_key_event(key_event, AccountOptions.CHANGE_NAME.value):
                self.change_name()
                show_menu = True
            
            if keyboard_utils.check_key_event(key_event, AccountOptions.BACK.value):
                print("Back to main menu")
                break           
    
    def change_name(self) -> None:
        '''
            Handles logic of changing account name
        '''
        new_name: str = input("Enter new name: ")
        show_menu: bool = True

        while len(new_name) < NAME_MIN_LENGTH or len(new_name) > NAME_MAX_LENGTH:
            print("Name must be between 1 and 20 characters, try again")
            new_name = input("Enter new name: ")

        while True:
            if show_menu:
                print("\nConfirm change?")
                print("[Y] Yes [N] No")
                show_menu = False
            
            key_event: KeyboardEvent = keyboard.read_event(suppress=True)

            if keyboard_utils.check_key_event(key_event, Confirmation.YES.value):
                self._name = new_name
                print("Name changed successfully")
                break
        
            if keyboard_utils.check_key_event(key_event, Confirmation.NO.value):
                print("Canceled name change")
                break
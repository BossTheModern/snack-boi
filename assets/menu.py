'''
    menu.py

    Module that handles menu navigation and action logic
'''
import os, copy, keyboard
from utils import consts
from utils import keyboard_utils
from typing import List, Callable
from assets.save_file import SaveFile
from keyboard import KeyboardEvent
from assets.printer.fancy_printer import FancyPrinter
from assets.levels.level import Level
from assets.menu_front import MenuFront
from assets.shop.shop import Shop
from account.account import Account
from assets.shop.shop_item import ShopItem
from utils.consts import NAME_MIN_LENGTH
from utils.consts import NAME_MAX_LENGTH

class Menu:
    _valid_options_inputs: List[str] = ['1', '2']
    _valid_level_menu_inputs: List[str] = ['A', 'D', 'S']
    _game_modes: List[str] = ['classic', 'endless']
    game_loop: Callable[[List[List[str]]], None]
    _menu_front: MenuFront = MenuFront()
    _shop: Shop = Shop()
    _account: Account
    
    _fancy_print: FancyPrinter = FancyPrinter()

    def __init__(self, game_loop: Callable[[List[List[str]]], None], account: Account) -> None:
        self.game_loop = game_loop
        self._account = account
    
    def print_welcome_screen(self) -> None:
        '''
            prints the welcome screen that runs upon booting the game
        '''
        text: str = "Welcome to snack boi!\n" \
                    "Press any button to continue"

        self._fancy_print.print_text(text)
    
    def version_log(self) -> None:
        '''
            Prints the contents of the version log file and prompts the user
            to return to menu
        '''
        display_text: bool = True
        key_event: KeyboardEvent
        
        while True:
            if display_text:
                self._menu_front.print_version_log()
                print("\nPress Q to return to menu")
                display_text = False
            
            key_event = keyboard.read_event(suppress=True)
            
            if keyboard_utils.check_key_event(key_event, 'q'):
                break
        
        print("Returning to menu")

    def selected_level(self, levels: List[Level]) -> Level:
        for level in levels:
            if level._selected:
                return level

    def mode_selection_menu(self, levels: List[Level]) -> None:
        '''
            Logic for handling mode selection and displaying its menu
        '''
        show_menu: bool = True

        while True:
            if show_menu:
                self._menu_front.print_mode_selection_menu()
                show_menu = False
                
            key_event: KeyboardEvent = keyboard.read_event(suppress=True)

            if keyboard_utils.check_key_event(key_event, '1'):
                self.levels_menu(levels, self._game_modes[0])
                show_menu = True
                break
            elif keyboard_utils.check_key_event(key_event, '2'):
                self.levels_menu(levels, self._game_modes[1])
                show_menu = True
                break
            elif keyboard_utils.check_key_event(key_event, '3'):
                print("Returning to main menu")
                show_menu = True
                break 
    
    def fetch_progress(self, save_file: SaveFile) -> None:
        '''
            Fetches progress and displays it on the menu
        '''
        key_event: KeyboardEvent
        show_text: bool = True

        if os.path.exists(save_file._file_path):
            while True:
                if show_text:
                    self._menu_front.print_progress(save_file)
                    print("Press any key to continue")
                    show_text = False

                key_event = keyboard.read_event(suppress=True)    
                if key_event.event_type == keyboard.KEY_DOWN:
                    break
        else:
            while True:
                if show_text:
                    self._menu_front.print_warning()
                    print("Press any key to continue")
                    show_text = False

                key_event = keyboard.read_event(suppress=True)    
                if key_event.event_type == keyboard.KEY_DOWN:
                    break
        
        print("Returning to main menu")
        

    def game_options(self, board: List[Level], save_file: SaveFile) -> None:
        '''
            Logic for handling options and displaying its menu
        '''
        show_menu: bool = True
        show_save_menu: bool = True
        key_event: KeyboardEvent
        
        def delete_file() -> None:
            key_event: KeyboardEvent

            print("----------[WARNING]----------")
            print("This will delete your save file and progression will be lost upon restart")
            print("Are you sure you want to delte your save file? (y/n)")

            while True: 
                key_event = keyboard.read_event(suppress=True)
                if key_event.event_type == keyboard.KEY_DOWN and key_event.name in ['y', 'n']:
                    break

            save_file.delete() if keyboard_utils.check_key_event(key_event, 'y') else print("Save file not deleted")

        # Game options menu loop
        while True:
            if show_menu:
                self._menu_front.print_game_options(self._valid_options_inputs)
                show_menu = False

            key_event = keyboard.read_event(suppress=True)

            if keyboard_utils.check_key_event(key_event, '2'):
                break
            
            # Manage save file options
            if keyboard_utils.check_key_event(key_event, '1'): 
                show_menu = True
                
                while True:
                    if show_save_menu:
                        self._menu_front.print_save_file_options()
                        show_save_menu = False
                    
                    key_event = keyboard.read_event(suppress=True)
                    
                    if keyboard_utils.check_key_event(key_event, '1'):
                        print("Loading current progress...")
                        self.fetch_progress(save_file)
                        show_save_menu = True
                    
                    if keyboard_utils.check_key_event(key_event, '2'):
                        print("Saving current progress...")
                        save_file.save(board)
                        show_save_menu = True
                    
                    if keyboard_utils.check_key_event(key_event, '3'):
                        delete_file()
                        show_save_menu = True
                    
                    if keyboard_utils.check_key_event(key_event, '4'):
                        print("Returning to options menu")
                        show_save_menu = True
                        break

        print("Returning to main menu")
    
    def navigate_selection(self, input: KeyboardEvent, levels: List[Level]) -> None:
        '''
            Logic for naviagting selection of levels from existing gamemodes
        '''
        # Find index of currently selected level
        current_lvl_index: int = 0

        for level in levels:
            if level._selected:
                break
            current_lvl_index += 1
        
        # Handle keyboard input
        if keyboard_utils.check_key_event(input, 'a'):
            if current_lvl_index - 1 < 0:
                return
            
            levels[current_lvl_index-1]._selected = True
            levels[current_lvl_index]._selected = False
        elif keyboard_utils.check_key_event(input, 'd'):
            if current_lvl_index + 1 > len(levels)-1:
                return
            
            levels[current_lvl_index+1]._selected = True
            levels[current_lvl_index]._selected = False
    
    # UNDER DEVELOPMENT: Merging menu displays for existing gamemodes
    def levels_menu(self, levels: List[Level], mode: str) -> None:
        '''
            Logic for handling endless levels navigation and selection
        '''
        selected_level: Level
        original_grid: List[List[str]]
        show_menu: bool = True

        while True:
            if show_menu:
                match mode:
                    case 'classic': self._menu_front.print_level_menu(levels)
                    case 'endless': self._menu_front.print_endless_levels_menu(levels)
                show_menu = False

            key_event: KeyboardEvent = keyboard.read_event(suppress=True)

            if keyboard_utils.check_key_event(key_event, 'q'):
                print("Going back to main menu")
                break

            if keyboard_utils.check_key_event(key_event, 's'):
                selected_level = self.selected_level(levels)

                if mode == self._game_modes[0]:
                    if selected_level._unlocked:
                        original_grid = copy.deepcopy(selected_level._level_board)
                        print(f"Running {selected_level._level_name}")
                        self.game_loop(original_grid, self._game_modes[0])
                        break
                    else: 
                        print("Level is locked, clear the previous level first")

                if mode == self._game_modes[1]:
                    if selected_level._cleared:
                        original_grid = copy.deepcopy(selected_level._level_board)
                        print(f"Running {selected_level._level_name}")
                        self.game_loop(original_grid, self._game_modes[1])
                        break
                    else: 
                        print("Level is locked, clear the corresponding level in classic mode first")
                
            if keyboard_utils.check_key_event(key_event, 'a') or keyboard_utils.check_key_event(key_event, 'd'):
                self.navigate_selection(key_event, levels)
                show_menu = True

    def shop_menu(self) -> None:
        '''
            Logic for handling shop menu display and navigation
        '''
        show_menu: bool = True

        while True:
            if show_menu:
                self._shop.print_shop_menu(self._account)
                show_menu = False
            
            key_event: KeyboardEvent = keyboard.read_event(suppress=True)
            if keyboard_utils.check_key_event(key_event, 'q'):
                print("Returning to main menu")
                break

            if key_event.event_type == keyboard.KEY_DOWN and key_event.name in [str(x+1) for x in range(len(self._shop._shop_items))]:
                self.shop_item_details_menu(int(key_event.name))
                show_menu = True
            


    def shop_item_details_menu(self, item_num: int) -> None:
        '''
            Logic for handling shop item detals menu display and navigation
        '''
        show_menu: bool = True

        while True:
            if show_menu:
                self._shop.show_shop_item_details(item_num)
                show_menu = False
            
            key_event: KeyboardEvent = keyboard.read_event(suppress=True)

            if keyboard_utils.check_key_event(key_event, 'q'):
                print("Returning to shop menu\n\n")
                break

            if keyboard_utils.check_key_event(key_event, 'b'):
                # TODO: Create logic for buying item
                self.shop_item_purchase(item_num)
                break
    
    def shop_item_purchase(self, item_num: int) -> None:
        '''
            Handles the logic of purchasing the shop item,
            such as linking button presses to corresponding actions
            such as purchasing or cancelling
        '''
        show_menu: bool = True
        item_num -= 1
        current_balance: int = self._account._points_balance
        price: int = self._shop._shop_items[item_num]._price
        shop_item: ShopItem = self._shop._shop_items[item_num]
        shop_item_limit: int = shop_item._limit
        acc_shop_items: List[ShopItem] = self._account._owned_shop_items
        shop_item_stock: int = acc_shop_items[item_num]._stock if len(acc_shop_items) > 0 else 0

        # Reject preemptively if the user has insufficient funds
        # or if item stock has reached limit
        if current_balance < price:
            print("Insufficient funds, try again later\n\n")
            return
        
        if shop_item_stock == shop_item_limit:
            print("Stock limit reached, try again later\n\n")
            return

        
        while True:
            if show_menu:
                self._shop.purchase_item_menu(item_num+1)
                show_menu = False
            
            key_event: KeyboardEvent = keyboard.read_event(suppress=True)

            if keyboard_utils.check_key_event(key_event, 'y'):
                if not self.shop_item_exists(shop_item):                    
                    self._account._owned_shop_items.append(shop_item)

                shop_item._stock += 1
                self._account._points_balance -= price
                print("Purchase successful\n\n")
                break
            
            if keyboard_utils.check_key_event(key_event, 'n'):
                print("Canceled purchase\n\n")
                break
    
    def shop_item_exists(self, shop_item: ShopItem) -> bool:
        owned_shop_items: List[ShopItem] = self._account._owned_shop_items

        if len(owned_shop_items) == 0:
            return False

        for item in owned_shop_items:
            if item._name == shop_item._name:
                return True

        return False
    
    def prompt_name(self) -> None:
        '''
            Prompts the user to enter their name upon first boot
            of the game
        '''
        new_name: str = input("Enter your name: ")

        # input sanitization
        while len(new_name) < NAME_MIN_LENGTH or len(new_name) > NAME_MAX_LENGTH:
            print("Name must be between 1 and 20 characters, try again")
            new_name = input("Enter your name: ")

        self._account._name = new_name
        print(f"Welcome to the game, {self._account._name}!")
    
    def prompt_powerup_selection(self, owned_powerups: List[ShopItem]) -> int:
        '''
            Handling logic for prompting user to select a powerup
            before starting game
        '''
        index: int = 0
        show_menu: bool = True

        while True:
            if show_menu:
                self._menu_front.print_owned_powerups(owned_powerups, index)
                show_menu = False

            key_event: KeyboardEvent = keyboard.read_event(suppress=True)

            if keyboard_utils.check_key_event(key_event, 'w') and index > 0:
                index -= 1
                show_menu = True

            if keyboard_utils.check_key_event(key_event, 's') and index < len(owned_powerups)-1:
                index += 1
                show_menu = True

            if keyboard_utils.check_key_event(key_event, 'e'):
                break

            if keyboard_utils.check_key_event(key_event, 'q'):
                index = -1
                break

        return index
        
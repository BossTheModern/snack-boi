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
from assets.shop.shop_items import ShopItems
from boards.board import Board
from assets.enums.enums import Gamemodes, SaveFileOptions, ModeSelection, OptionsSelection, Confirmation, StdNavigationOptions, StdPowerupNavigationsOptions
from assets.shop.shop_items_collection import shop_item_collection
from assets.shop.shop_items import ShopItems
from utils.consts import NAME_MIN_LENGTH
from utils.consts import NAME_MAX_LENGTH
from utils.consts import EMPTY_SHOP_ITEM
from utils.menu_utils import make_pages
from utils import terminal_clearing



class Menu:
    game_loop: Callable[[Board, str], None]
    _menu_front: MenuFront = MenuFront()
    _shop: Shop = Shop()
    _account: Account
    
    _fancy_print: FancyPrinter = FancyPrinter()

    def __init__(self, game_loop: Callable[[Board, str], None], account: Account) -> None:
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
                terminal_clearing.clear_terminal()
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
                terminal_clearing.clear_terminal()
                self._menu_front.print_mode_selection_menu()
                show_menu = False
                
            key_event: KeyboardEvent = keyboard.read_event(suppress=True)

            if keyboard_utils.check_key_event(key_event, ModeSelection.CLASSIC_MODE.value):
                self.levels_menu(levels, Gamemodes.CLASSIC.value)
                show_menu = True
                break
            elif keyboard_utils.check_key_event(key_event, ModeSelection.ENDLESS_MODE.value):
                self.levels_menu(levels, Gamemodes.ENDLESS.value)
                show_menu = True
                break
            elif keyboard_utils.check_key_event(key_event, ModeSelection.BACK.value):
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
                if key_event.event_type == keyboard.KEY_DOWN and key_event.name in Confirmation._value2member_map_:
                    break

            save_file.delete() if keyboard_utils.check_key_event(key_event, Confirmation.YES.value) else print("Save file not deleted")

        # Game options menu loop
        while True:
            if show_menu:
                terminal_clearing.clear_terminal()
                self._menu_front.print_game_options()
                show_menu = False

            key_event = keyboard.read_event(suppress=True)

            if keyboard_utils.check_key_event(key_event, OptionsSelection.BACK.value):
                break
            
            # Manage save file options
            if keyboard_utils.check_key_event(key_event, OptionsSelection.MANAGE_SAVE_FILE.value): 
                show_menu = True
                
                while True:
                    if show_save_menu:
                        terminal_clearing.clear_terminal()
                        self._menu_front.print_save_file_options()
                        show_save_menu = False
                    
                    key_event = keyboard.read_event(suppress=True)
                    
                    if keyboard_utils.check_key_event(key_event, SaveFileOptions.LOAD_PROGRESS.value):
                        print("Loading current progress...")
                        self.fetch_progress(save_file)
                        show_save_menu = True
                    
                    if keyboard_utils.check_key_event(key_event, SaveFileOptions.SAVE_PROGRESS.value):
                        print("Saving current progress...")
                        save_file.save(board)
                        show_save_menu = True
                    
                    if keyboard_utils.check_key_event(key_event, SaveFileOptions.DELETE_SAVE.value):
                        delete_file()
                        show_save_menu = True
                    
                    if keyboard_utils.check_key_event(key_event, SaveFileOptions.BACK.value):
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
        if keyboard_utils.check_key_event(input, StdNavigationOptions.LEFT.value):
            if current_lvl_index - 1 < 0:
                return
            
            levels[current_lvl_index-1]._selected = True
            levels[current_lvl_index]._selected = False
        elif keyboard_utils.check_key_event(input, StdNavigationOptions.RIGHT.value):
            if current_lvl_index + 1 > len(levels)-1:
                return

            levels[current_lvl_index+1]._selected = True
            levels[current_lvl_index]._selected = False

    def levels_menu(self, levels: List[Level], mode: str) -> None:
        '''
            Logic for handling endless levels navigation and selection
        '''
        selected_level: Level
        original_grid: Board
        show_menu: bool = True

        while True:
            if show_menu:
                terminal_clearing.clear_terminal()
                self._menu_front.print_levels_menu(levels, mode)
                show_menu = False

            key_event: KeyboardEvent = keyboard.read_event(suppress=True)

            if keyboard_utils.check_key_event(key_event, StdNavigationOptions.BACK.value):
                print("Going back to main menu")
                break

            if keyboard_utils.check_key_event(key_event, StdNavigationOptions.SELECT.value):
                selected_level = self.selected_level(levels)

                if mode == Gamemodes.CLASSIC.value:
                    if selected_level._unlocked:
                        original_grid = copy.deepcopy(selected_level._level_board)
                        print(f"Running {selected_level._level_name}")
                        self.game_loop(original_grid, Gamemodes.CLASSIC.value)
                        break
                    else: 
                        print("Level is locked, clear the previous level first")

                if mode == Gamemodes.ENDLESS.value:
                    if selected_level._cleared:
                        original_grid = copy.deepcopy(selected_level._level_board)
                        print(f"Running {selected_level._level_name}")
                        self.game_loop(original_grid, Gamemodes.ENDLESS.value)
                        break
                    else: 
                        print("Level is locked, clear the corresponding level in classic mode first")
                
            if keyboard_utils.check_key_event(key_event, StdNavigationOptions.LEFT.value) or keyboard_utils.check_key_event(key_event, StdNavigationOptions.RIGHT.value):
                self.navigate_selection(key_event, levels)
                show_menu = True

    def shop_menu(self) -> None:
        '''
            Logic for handling shop menu display and navigation
        '''
        show_menu: bool = True
        
        # Makes pages for navigation
        pages: List[ShopItems] = make_pages(ShopItems(shop_item_collection.get_items()))
        current_page_index: int = 0
        current_page: ShopItems = ShopItems()
        message: str = ""

        while True:
            current_page = pages[current_page_index]
            if show_menu:
                terminal_clearing.clear_terminal()
                self._shop.print_shop_menu(self._account, pages[current_page_index])
                if message != "":
                    print(message)
                    message = ""
                show_menu = False
            
            key_event: KeyboardEvent = keyboard.read_event(suppress=True)
            if keyboard_utils.check_key_event(key_event, StdNavigationOptions.BACK.value):
                print("Returning to main menu")
                break

            if keyboard_utils.check_key_event(key_event, StdNavigationOptions.LEFT.value):
                if current_page_index > 0:
                    current_page_index -= 1
                show_menu = True

            if keyboard_utils.check_key_event(key_event, StdNavigationOptions.RIGHT.value):
                if current_page_index < len(pages)-1:
                    current_page_index += 1
                show_menu = True


            if key_event.event_type == keyboard.KEY_DOWN and key_event.name in [str(x+1) for x in range(current_page.size())]:
                message = self.shop_item_details_menu(current_page.get_items()[int(key_event.name)-1])
                show_menu = True
            


    def shop_item_details_menu(self, selected_item: ShopItem) -> str:
        '''
            Logic for handling shop item detals menu display and navigation
        '''
        show_menu: bool = True
        message: str = ""

        while True:
            if show_menu:
                terminal_clearing.clear_terminal()
                self._shop.show_shop_item_details(selected_item)
                show_menu = False
            
            key_event: KeyboardEvent = keyboard.read_event(suppress=True)

            if keyboard_utils.check_key_event(key_event, 'q'):
                return "Returned to shop menu\n\n"

            if keyboard_utils.check_key_event(key_event, 'b'):
                message = self.shop_item_purchase(selected_item)
                return message
    
    def shop_item_purchase(self, selected_item: ShopItem) -> str:
        '''
            Handles the logic of purchasing the shop item,
            such as linking button presses to corresponding actions
            such as purchasing or cancelling
        '''
        show_menu: bool = True
        current_balance: int = self._account._points_balance
        price: int = selected_item._price
        shop_item: ShopItem = selected_item
        shop_item_limit: int = shop_item._limit
        acc_shop_items: ShopItems = self._account._owned_shop_items

        acc_shop_item: ShopItem = EMPTY_SHOP_ITEM
        for item in acc_shop_items.get_items():
            if item._name == shop_item._name:
                acc_shop_item = item

        shop_item_stock: int = acc_shop_item._stock if acc_shop_items.size() > 0 else 0

        # Reject preemptively if the user has insufficient funds
        # or if item stock has reached limit
        if current_balance < price:
            return "Insufficient funds, try again later\n\n"
        
        if shop_item_stock == shop_item_limit:
            return "Stock limit reached, try again later\n\n"

        
        while True:
            if show_menu:
                terminal_clearing.clear_terminal()
                self._shop.purchase_item_menu(selected_item)
                show_menu = False
            
            key_event: KeyboardEvent = keyboard.read_event(suppress=True)

            if keyboard_utils.check_key_event(key_event, Confirmation.YES.value):
                if not self.shop_item_exists(shop_item):                    
                    self._account._owned_shop_items.add_item(shop_item)

                shop_item._stock += 1
                self._account._points_balance -= price
                return "Purchase successful\n\n"
            
            if keyboard_utils.check_key_event(key_event, Confirmation.NO.value):
                return "Canceled purchase\n\n"
    
    def shop_item_exists(self, shop_item: ShopItem) -> bool:
        owned_shop_items: ShopItems = self._account._owned_shop_items

        if owned_shop_items.is_empty():
            return False

        for item in owned_shop_items.get_items():
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
                terminal_clearing.clear_terminal()
                self._menu_front.print_owned_powerups(owned_powerups, index)
                show_menu = False

            key_event: KeyboardEvent = keyboard.read_event(suppress=True)

            if keyboard_utils.check_key_event(key_event, StdPowerupNavigationsOptions.UP.value) and index > 0:
                index -= 1
                show_menu = True

            if keyboard_utils.check_key_event(key_event, StdPowerupNavigationsOptions.DOWN.value) and index < len(owned_powerups)-1:
                index += 1
                show_menu = True

            if keyboard_utils.check_key_event(key_event, StdPowerupNavigationsOptions.SELECT.value):
                break

            if keyboard_utils.check_key_event(key_event, StdPowerupNavigationsOptions.SKIP.value):
                index = -1
                break

        return index
        
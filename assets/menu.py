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

class Menu:
    _valid_options_inputs: List[str] = ['1', '2']
    _valid_level_menu_inputs: List[str] = ['A', 'D', 'S']
    _game_modes: List[str] = ['classic', 'endless']
    game_loop: Callable[[List[List[str]]], None]
    _menu_front: MenuFront = MenuFront()
    
    _fancy_print: FancyPrinter = FancyPrinter()

    def __init__(self, game_loop: Callable[[List[List[str]]], None]) -> None:
        self.game_loop = game_loop
    
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
'''
    menu_front.py

    contains menu print commands for various game menus and displays
'''
from typing import List
from utils import consts
from assets.levels.level import Level
from assets.save_file import SaveFile

class MenuFront:
    _select_char: str = '>'
    _lock_char: str = '(locked)'
    _wrap_limit: int = 5
    _valid_modes_inputs: List[str] = ['1', '2', '3']

    def print_game_menu(self, version: str, menu_options: List[str]) -> None:
        '''
            Prints the main menu of the game
        '''
        print("-----[Snack boi]-----")
        print(f"[{menu_options[0]}] Start Game")
        print(f"[{menu_options[1]}] Options")
        print(f"[{menu_options[2]}] Version log")
        print(f"[{menu_options[3]}] Quit")
        print("version:", version)
        print("---------------------")
    
    def print_version_log(self) -> None:
        '''
            Prints the contents of version log file
        '''
        file_content: str
        try:
            with open(consts.VERSION_LOG_FILE_PATH) as file:
                file_content = file.read()

            print(file_content)
        except OSError:
            print("Error: Could not read file")
    
    def print_endless_levels_menu(self, levels: List[Level]) -> None:
        '''
            Prints menu for levels on endless mode
        '''
        counter: int = 0

        print("-----[ENDLESS MODE LEVELS]-----\n")
        for level in levels:
            if level._selected:
                print(self._select_char, end="")
            print(f"[{level._level_name}]", end="")
            if not level._cleared:
                print(self._lock_char, end="")
            print(" ", end="")

            counter += 1
            if counter == self._wrap_limit:
                print()
                counter = 0
        print()
        print("\n[A] Move left [D] Move right [S] Select")
        print("[Q] Back to main menu")
        print("-------------------------------")
    
    def print_level_menu(self, levels: List[Level]) -> None:
        '''
            Prints menu for levels on classic mode
        '''
        counter: int = 0

        print("-----[CLASSIC MODE LEVELS]-----\n")
        for level in levels:
            if level._selected:
                print(self._select_char, end="")
            print(f"[{level._level_name}]", end="")
            if not level._unlocked:
                print(self._lock_char, end="")
            print(" ", end="")

            counter += 1
            if counter == self._wrap_limit:
                print()
                counter = 0
        print()
        print("\n[A] Move left [D] Move right [S] Select")
        print("[Q] Back to main menu")
        print("---------------------")
    
    def print_mode_selection_menu(self) -> None:
            print("-----[MODES]-----")
            print(f"[{self._valid_modes_inputs[0]}] Classic Mode")
            print(f"[{self._valid_modes_inputs[1]}] Endless mode")
            print(f"[{self._valid_modes_inputs[2]}] Back to main menu")
            print("-----------------")
    
    def print_progress(self, save_file: SaveFile) -> None:
        print("-----[Currently Saved Progress]-----")
        print(f"Levels unlocked: {save_file._data['highest_unlocked_lvl']}")
        print(f"Levels cleared: {save_file._data['highest_cleared_lvl']}")
        print("Note: This shows the currently saved progress, not the actual current game progress")
        print("------------------------------------")
    
    def print_warning(self) -> None:
        print("--------------[WARNING]--------------")
        print("No file found, nothing to show here")
        print("Create a save file and try again")
        print("-------------------------------------")

    def print_save_file_options(self) -> None:
        print("-----[Save file options]-----")
        print("[1] Load current progress")
        print("[2] Save current progress")
        print("[3] Delete save file")
        print("[4] Back to options menu")
        print("-----------------------------")
    
    def print_game_options(self, valid_options_inputs: List[int]) -> None:
        print("-----[Options]-----")
        print(f"[{valid_options_inputs[0]}] Manage save file")
        print(f"[{valid_options_inputs[1]}] Back to main menu")
        print("-------------------")
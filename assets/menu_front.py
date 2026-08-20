'''
    menu_front.py

    contains menu print commands for various game menus and displays
'''
from typing import List
from utils import consts
from assets.levels.level import Level
from assets.save_file import SaveFile
from assets.shop.shop_item import ShopItem
from assets.enums.enums import MainMenuOptions, ModeSelection, OptionsSelection, SaveFileOptions, StdNavigationOptions, Gamemodes

class MenuFront:
    _select_char: str = '>'
    _lock_char: str = '(locked)'
    _wrap_limit: int = 5

    def print_game_menu(self) -> None:
        '''
            Prints the main menu of the game
        '''
        print("-----[Snack boi]-----")
        print(f"[{MainMenuOptions.START_GAME.value}] Start Game")
        print(f"[{MainMenuOptions.SHOP_MENU.value}] Shop")
        print(f"[{MainMenuOptions.ACCOUNT.value}] Account")
        print(f"[{MainMenuOptions.OPTIONS.value}] Options")
        print(f"[{MainMenuOptions.VERSION_LOG.value}] Version log")
        print(f"[{MainMenuOptions.QUIT.value}] Quit")
        print("version:", consts.VERSION)
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
    
    def print_levels_menu(self, levels: List[Level], mode: str) -> None:
        '''
            Prints menu for levels on classic mode
        '''
        counter: int = 0
        lock_condition: bool = False

        if mode == Gamemodes.CLASSIC.value:
            print("-----[CLASSIC MODE LEVELS]-----\n")
        if mode == Gamemodes.ENDLESS.value:
            print("-----[ENDLESS MODE LEVELS]-----\n")
        
        for level in levels:
            if level._selected:
                print(self._select_char, end="")
            print(f"[{level._level_name}]", end="")

            lock_condition = not level._unlocked if mode == Gamemodes.CLASSIC.value else not level._cleared

            if lock_condition:
                print(self._lock_char, end="")
            print(" ", end="")

            counter += 1
            if counter == self._wrap_limit:
                print()
                counter = 0
        print()
        print(f"\n[{StdNavigationOptions.LEFT.value.upper()}] Move left [{StdNavigationOptions.RIGHT.value.upper()}] Move right [{StdNavigationOptions.SELECT.value.upper()}] Select")
        print(f"[{StdNavigationOptions.BACK.value.upper()}] Back to main menu")
        print("---------------------")
    
    def print_mode_selection_menu(self) -> None:
        print("-----[MODES]-----")
        print(f"[{ModeSelection.CLASSIC_MODE.value}] Classic Mode")
        print(f"[{ModeSelection.ENDLESS_MODE.value}] Endless mode")
        print(f"[{ModeSelection.BACK.value}] Back to main menu")
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
        print(f"[{SaveFileOptions.LOAD_PROGRESS.value}] Load current progress")
        print(f"[{SaveFileOptions.SAVE_PROGRESS.value}] Save current progress")
        print(f"[{SaveFileOptions.DELETE_SAVE.value}] Delete save file")
        print(f"[{SaveFileOptions.BACK.value}] Back to options menu")
        print("-----------------------------")
    
    def print_game_options(self) -> None:
        print("-----[Options]-----")
        print(f"[{OptionsSelection.MANAGE_SAVE_FILE.value}] Manage save file")
        print(f"[{OptionsSelection.BACK.value}] Back to main menu")
        print("-------------------")
    
    def print_owned_powerups(self, owned_powerups: List[ShopItem], selected_index: int) -> None:
        print(f"{'[SELECT SHOP POWERUP]':-^50}")
        for index, powerup in enumerate(owned_powerups):
            print('> ' if selected_index == index else '', powerup._name)
        print(f"{'':-<50}")
        print("[W] Up [S] Down [E] Select [Q] Skip")

'''
    game_utils.py

    contains utility functions for game loop
'''

from typing import List
from utils import consts
from assets.printer.fancy_printer import FancyPrinter
from assets.text_collection import TextCollection
from assets.levels.level import Level
from assets.snacks.snack import Snack
from assets.shop.shop_item import ShopItem
from assets.enums.enums import Gamemodes, SnackTypes, MiscGameControls
from boards.board import Board
from account.account import Account

class GameUtils:
    def __init__(self, snack: Snack) -> None:
          self._snack: Snack = snack

          # Toggle text variables
          self._recon_spawned: bool = False
          self._traps_revealed: bool = False
          self._hunger_trap_eaten: bool = False
          self._parallel_trap_eaten: bool = False
          self._snack_eaten: bool = False
          self._fake_snack_eaten: bool = False
          self._super_snack_eaten: bool = False
          self._fancy_print: FancyPrinter = FancyPrinter()
          self._text_collection: TextCollection = TextCollection()

    def classic_display_current_state(self, board: Board, current_lvl_index: int, levels: List[Level]) -> None:
        print(f"--------[CLASSIC MODE - {levels[current_lvl_index]._level_name}]--------")
        board.display()
        print(f"{self._snack._count}/{levels[current_lvl_index]._win_cap} snacks eaten")
        
    def endless_display_current_state(self, board: Board, current_lvl_index: int, levels: List[Level]) -> None:
        print(f"--------[ENDLESS MODE - {levels[current_lvl_index]._level_name}]--------")
        board.display()
        print("Snack count:", self._snack._count)
        
    def classic_game_win(self, current_lvl_index: int, levels: List[Level], account: Account) -> None:
        '''
            Handles winning logic for classic game mode
        '''
        next_level_index: int
        print("You win! You have eaten enough snacks!")

        account._points_balance += levels[current_lvl_index]._reward
        print(f"{levels[current_lvl_index]._reward} points earned!")
        

        if current_lvl_index + 1 <= len(levels)-1:
            next_level_index = current_lvl_index + 1

            if not levels[next_level_index]._unlocked:
                levels[next_level_index]._unlocked = True
                print("Next level unlocked")

        if not levels[current_lvl_index]._cleared:
            print(f"Endless mode for {levels[current_lvl_index]._level_name} unlocked!")
            levels[current_lvl_index]._cleared = True
    
    def toggleText(self) -> None:
        '''
            Toggles text based on game conditions
        '''
        # Supplementary toggle text
        if self._recon_spawned:
            print("Oh, I see a powerup over there. Let's get it!") 
            self._recon_spawned = False

        if self._traps_revealed:
            print("I can see the traps plain as day!")
            self._traps_revealed = False
                
        if self._hunger_trap_eaten:
            print("Oh no! I feel so hungry...")
            self._hunger_trap_eaten = False
                
        if self._parallel_trap_eaten:
            print("Getting out of here, see ya later!")
            self._parallel_trap_eaten = False
                
        if self._snack_eaten:
            print("Nom nom")
            self._snack_eaten = False
                
        if self._fake_snack_eaten:
            print("What!? That snack was fake!")
            self._fake_snack_eaten = False
                
        if self._super_snack_eaten:
            print("Yum! That one was delicious!")
            self._super_snack_eaten = False
    
    def clear_toggle_text(self) -> None:
        '''
            Clears all toggle text variables
        '''
        self._recon_spawned = False
        self._traps_revealed = False
        self._hunger_trap_eaten = False
        self._parallel_trap_eaten = False
        self._snack_eaten = False
        self._fake_snack_eaten = False
        self._super_snack_eaten = False
    
    def intro_text_display(self, levels_unlocked: int, current_lvl_index: int) -> None:
        '''
            Displays intro text based on the current level unlocked
            TODO: Change the logic so it doesn't play on other levels
            than the intended level
        '''
        if levels_unlocked == 1 and current_lvl_index == 0:
            self._fancy_print.print_text_line(self._text_collection._start_intro)
        elif levels_unlocked == consts.NEW_SNACKS_START_LVL and current_lvl_index == consts.NEW_SNACKS_START_LVL - 1:
            self._fancy_print.print_text_line(self._text_collection._extra_snack_intro)
        elif levels_unlocked == consts.TRAP_START_LVL and current_lvl_index == consts.TRAP_START_LVL - 1:
            self._fancy_print.print_text_line(self._text_collection._traps_intro)
    
    def display_current_state(self, board: Board, current_lvl_index: int, 
                              levels: List[Level], game_mode: str, 
                              current_snack_type: str, recon_duration: int, recon_active: bool,
                              active_powerup: ShopItem) -> None:
        '''
            Displays the current state of the game basd on game mode
        '''
        match game_mode:
            case Gamemodes.CLASSIC.value:
                self.classic_display_current_state(board, current_lvl_index, levels)
            case Gamemodes.ENDLESS.value:
                self.endless_display_current_state(board, current_lvl_index, levels)
            case _:
                print("Nothing to display")
        
        print("Move by pressing (w/a/s/d) or press q to quit")
        print("Super snack spawned! Eat it for extra points!") if current_snack_type == SnackTypes.SUPER.value else None
        print(f"Recon duration: {recon_duration} moves") if recon_active else None
        self.display_active_powerup_status(active_powerup) if active_powerup._name != "None" else None
            
        # Supplementary toggle text
        self.toggleText()
    
    def display_active_powerup_status(self, active_powerup: ShopItem) -> None:
        print(f"{'':-<30}")
        print(f"Active powerup: {active_powerup._name} ({'ACTIVE' if active_powerup._active else 'INACTIVE'})")
        print(f"Current duration: {active_powerup._active_duration}")
        print(f"[{MiscGameControls.USE_POWERUP.value.upper()}] Activate")
        print(f"[{MiscGameControls.USE_RECALL.value.upper()}] Use recall") if active_powerup._name == "Recall" else None
    
    def set_snack_eaten(self, current_snack_type: str) -> None:
        '''
            Sets appropriate toggle text variables based on snack eaten
        '''
        match current_snack_type:
            case SnackTypes.NORMAL.value: self._snack_eaten = True
            case SnackTypes.SUPER.value: self._super_snack_eaten = True
            case SnackTypes.FAKE.value: self._fake_snack_eaten = True
'''
    game_utils.py

    contains utility functions for game loop
'''


from typing import List
from assets.levels.level import Level
from assets.snacks.snack import Snack
from boards.board_creator import draw_grid

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

    def classic_display_current_state(self, board: List[List[str]], current_lvl_index: int, levels: List[Level]) -> None:
        print(f"--------[CLASSIC MODE - {levels[current_lvl_index]._level_name}]--------")
        draw_grid(board)
        print(f"{self._snack._count}/{levels[current_lvl_index]._win_cap} snacks eaten")
        
    def endless_display_current_state(self, board: List[List[str]], current_lvl_index: int, levels: List[Level]) -> None:
        print(f"--------[ENDLESS MODE - {levels[current_lvl_index]._level_name}]--------")
        draw_grid(board)
        print("Snack count:", self._snack._count)
        
    def classic_game_win(self, current_lvl_index: int, levels: List[Level]) -> None:
        '''
            Handles winning logic for classic game mode
        '''
        next_level_index: int
        print("You win! You have eaten enough snacks!")

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
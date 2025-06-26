'''
    game_utils.py

    contains utility functions for game loop
'''


from typing import List
from assets.levels.level import Level
from assets.snacks.snack import Snack
from assets.snacks.snack_types import NormalSnack, FakeSnack, SuperSnack
from boards.board_creator import OBSTACLE_CHAR
from assets.player import Player
from boards.board_creator import draw_grid

class GameUtils:
    def __init__(self, snack: Snack) -> None:
          self._snack: Snack = snack

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
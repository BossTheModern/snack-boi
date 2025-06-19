'''
    recon_snack.py

    Handles logic for powerup recon snack
'''
from typing import List
import random
import os
import sys

current_dir: str = os.path.dirname(os.path.abspath(__file__))
parent_dir: str = os.path.join(current_dir)

sys.path.insert(0, parent_dir)

from traps import Trap

class ReconSnack:
    def __init__(self) -> None:
        self._position: List[int] = []
        self._entity_char: str = 'R'
        self._counter: int = 0
        self._max_number: int = 1
        self._required_eaten_snacks: int = 5
        self._eaten_counter: int = 0
        self._duration: int = 4 # Visible for n-1 moves (this case it's 3 moves)
        self._active: bool = False
        self._traps_revealed: bool = False
        self._spawned: bool = False

    def spawn(self, board: List[List[str]], occupied_positions: List[List[int]]) -> None:
        self._position = [random.randint(0, len(board)-1), random.randint(0, len(board)-1)]

        while self._position in occupied_positions or board[self._position[0]][self._position[1]] != ' ':
            self._position = [random.randint(0, len(board)-1), random.randint(0, len(board)-1)]
        
        board[self._position[0]][self._position[1]] = self._entity_char
    
    def reveal_position(self, board: List[List[str]], traps: List[Trap]) -> None:
        '''
            Reveals position of all traps on the board

            Args:
                board: board where the powerup spawns on
                traps: list of trap to reveal their position
        '''

        # Implement position reveal logic
        for trap in traps:
            trap.reveal_trap(board)
    
    def undo_effect(self, board: List[List[str]], traps: List[Trap]) -> None:
        for trap in traps:
            trap.hide(board)
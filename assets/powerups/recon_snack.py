'''
    recon_snack.py

    Handles logic for powerup recon snack
'''
import random
from typing import List
from assets.traps.traps import Trap
from boards.board import Board

class ReconSnack:
    def __init__(self) -> None:
        self._position: List[int] = []
        self._entity_char: str = 'Q'
        self._counter: int = 0
        self._max_number: int = 1
        self._required_eaten_snacks: int = 5
        self._eaten_counter: int = 0
        self._duration: int = 4 # Visible for n-1 moves (this case it's 3 moves)
        self._active: bool = False

    def spawn(self, board: Board, occupied_positions: List[List[int]]) -> None:
        self._position = [random.randint(0, board._width-1), random.randint(0, board._height-1)]

        while self._position in occupied_positions or board.at(self._position[0], self._position[1]) != ' ':
            self._position = [random.randint(0, board._width-1), random.randint(0, board._height-1)]
        
        board.set(self._position[0], self._position[1], self._entity_char)
        self._counter += 1
    
    def reveal_position(self, board: Board, traps: List[Trap]) -> None:
        '''
            Reveals position of all traps on the board

            Args:
                board: board where the powerup spawns on
                traps: list of trap to reveal their position
        '''

        # Implement position reveal logic
        for trap in traps:
            trap.reveal_trap(board)
        
        self._position.clear()
        self._active = True
    
    def undo_effect(self, board: Board, traps: List[Trap]) -> None:
        for trap in traps:
            trap.hide(board)
        
        self._eaten_counter = 0
        self._counter -= 1
        self._active = False
    
    def clear_data(self) -> None:
        '''
            Clears powerup data
        '''
        self._position.clear()
        self._eaten_counter = 0
        self._counter = 0
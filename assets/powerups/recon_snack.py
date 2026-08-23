'''
    recon_snack.py

    Handles logic for powerup recon snack
'''
from typing import List
from assets.traps.traps import Trap
from assets.spawnable.spawnable import Spawnable
from boards.board import Board
from assets.position.position2d import Position2D

class ReconSnack(Spawnable):
    def __init__(self) -> None:
        super().__init__('Q')
        self._counter: int = 0
        self._max_number: int = 1
        self._required_eaten_snacks: int = 5
        self._eaten_counter: int = 0
        self._duration: int = 4 # Visible for n-1 moves (this case it's 3 moves)
        self._active: bool = False

    def spawn(self, board: Board, occupied_positions: List[Position2D]) -> None:
        super().spawn(board, occupied_positions)
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
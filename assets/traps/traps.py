'''
    traps.py

    Parent class containing methods that is shared across all traps
'''
from typing import List
from boards.board import Board
from assets.position.position2d import Position2D
import random

class Trap:
    revealed: bool = False

    def __init__(self) -> None:
        self._position: Position2D = Position2D()

    def spawn_trap(self, board: Board, occupied_positions: List[Position2D]) -> None:
        '''
            Spawns a trap on the board at a random available position. The
            traps are hidden by default
            Args:
                board: The board where the trap will be spawned.     
        '''
        random_x: int = random.randint(0, board._width-1)
        random_y: int = random.randint(0, board._height-1)
        self._position.set(random_x, random_y)

        while self._position in occupied_positions or board.at(self._position.x, self._position.y) != ' ':
            random_x = random.randint(0, board._width-1)
            random_y = random.randint(0, board._height-1)
            self._position.set(random_x, random_y)

        if self.revealed:
            board.set(self._position.x, self._position.y, self._trap_entity)
    
    def reveal_trap(self, board: Board) -> None:
        board.set(self._position.x, self._position.y, self._trap_entity)
        self.revealed = True
    
    def hide(self, board: Board) -> None:
        board.set(self._position.x, self._position.y, ' ')
        self.revealed = False
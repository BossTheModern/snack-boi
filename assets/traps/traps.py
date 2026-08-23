'''
    traps.py

    Parent class containing methods that is shared across all traps
'''
from typing import List
from boards.board import Board
from assets.position.position2d import Position2D
from assets.spawnable.spawnable import Spawnable

class Trap(Spawnable):
    revealed: bool = False
    
    def spawn(self, board: Board, occupied_positions: List[Position2D]) -> None:
        super().spawn(board, occupied_positions, hidden=True)

        if self.revealed:
            board.set(self._position.x, self._position.y, self._entity)

    def reveal_trap(self, board: Board) -> None:
        board.set(self._position.x, self._position.y, self._entity)
        self.revealed = True
    
    def hide(self, board: Board) -> None:
        board.set(self._position.x, self._position.y, ' ')
        self.revealed = False
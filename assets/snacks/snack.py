'''
    snack.py

    Parent class containing fields and methods that is shared across all types
    of snacks
'''
from typing import List
import random

class Snack:
    _position: List[int] = [0, 0]
    _count: int = 0
    _type: str = ''
    
    def spawn_snack(self, board: List[List[str]], occupied_positions: List[List[int]]) -> None:
        '''
            spawns snack on the grid

            Args:
                board: The board where the snack will be spawned.
        '''
        self._position = [random.randint(0, len(board)-1), random.randint(0, len(board)-1)]
        
        while self._position in occupied_positions or board[self._position[0]][self._position[1]] != ' ':
            self._position = [random.randint(0, len(board)-1), random.randint(0, len(board)-1)]
        board[self._position[0]][self._position[1]] = self._entity
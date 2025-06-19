'''
    dimension_exit.py

    handles logic for spawning parallel dimension exit
'''
from typing import List
import random

class DimensionExit:
    def __init__(self) -> None:
        self._position: List[int] = []
        self._enitity_char: str = 'E'
    
    def spawn(self, board: List[List[str]]) -> None:
        '''
            Spawns exit on the parallel dimension
        '''
        self._position = [random.randint(0, len(board)-1), random.randint(0, len(board)-1)]

        while board[self._position[0]][self._position[1]] != ' ':
            self._position = [random.randint(0, len(board)-1), random.randint(0, len(board)-1)]
        
        board[self._position[0]][self._position[1]] = self._enitity_char
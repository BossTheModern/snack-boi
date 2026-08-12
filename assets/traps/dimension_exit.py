'''
    dimension_exit.py

    handles logic for spawning parallel dimension exit
'''
from typing import List
from boards.board import Board
import random

class DimensionExit:
    def __init__(self) -> None:
        self._position: List[int] = []
        self._enitity_char: str = 'E'
    
    def spawn(self, board: Board) -> None:
        '''
            Spawns exit on the parallel dimension
        '''
        self._position = [random.randint(0, board._width-1), random.randint(0, board._height-1)]

        while board.at(self._position[0], self._position[1]) != ' ':
            self._position = [random.randint(0, board._width-1), random.randint(0, board._height-1)]
        
        board.set(self._position[0], self._position[1], self._enitity_char)
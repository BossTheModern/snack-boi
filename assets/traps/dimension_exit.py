'''
    dimension_exit.py

    handles logic for spawning parallel dimension exit
'''
from typing import List
from boards.board import Board
from assets.position.position2d import Position2D 
import random

class DimensionExit:
    def __init__(self) -> None:
        self._position: Position2D = Position2D()
        self._enitity_char: str = 'E'
    
    def spawn(self, board: Board) -> None:
        '''
            Spawns exit on the parallel dimension
        '''
        random_x: int = random.randint(0, board._width-1)
        random_y: int = random.randint(0, board._height-1)
        self._position.set(random_x, random_y)

        while board.at(self._position.x, self._position.y) != ' ':
            random_x = random.randint(0, board._width-1)
            random_y = random.randint(0, board._height-1)
            self._position.set(random_x, random_y)
        
        board.set(self._position.x, self._position.y, self._enitity_char)
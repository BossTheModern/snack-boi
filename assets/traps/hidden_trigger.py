'''
    hidden_trigger.py

    handles logic for spawning hidden trigger on the parallel dimension
'''
from typing import List
from boards.board import Board
from assets.position.position2d import Position2D
import random

class HiddenTrigger:
    def __init__(self) -> None:
        self._position: Position2D = Position2D()
        self._entity_char: str = 'T'
    
    def spawn(self, board: Board) -> None:
        '''
            Spawns the hidden trigger on the parallel dimension
        '''
        random_x: int = random.randint(0, board._width-1)
        random_y: int = random.randint(0, board._height-1)
        self._position.set(random_x, random_y)

        while board.at(self._position.x, self._position.y) != ' ':
            random_x = random.randint(0, board._width-1)
            random_y = random.randint(0, board._height-1)
            self._position.set(random_x, random_y)
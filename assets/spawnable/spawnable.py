'''
    spawnable.py

    parent class enapsulating all spawnable entities with the ability 
    to spawn in a random position on the board
'''
from assets.position.position2d import Position2D
from boards.board import Board
from typing import List
import random

class Spawnable:
    def __init__(self, entity: str = '') -> None:
        self._position: Position2D = Position2D()
        self._entity: str = entity

    def spawn(self, board: Board, occupied_positions: List[Position2D] = [], hidden: bool = False) -> None:
        '''
            randomly assigns a position to spawnable with the option of
            hiding the entity from the board
        '''
        random_x: int = random.randint(0, board._width-1)
        random_y: int = random.randint(0, board._height-1)
        self._position.set(random_x, random_y)
        
        while self._position in occupied_positions or not board.is_available_at(self._position):
            random_x = random.randint(0, board._width-1)
            random_y = random.randint(0, board._height-1)
            self._position.set(random_x, random_y)

        if not hidden:
            board.set(self._position.x, self._position.y, self._entity)
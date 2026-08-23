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

    def spawn(self, board: Board, occupied_positions: List[Position2D] = []) -> None:
        '''
            randomly assigns a position to spawnable

            NOTE: This only assigns a random position to spawnable and does not
            add the entity explicitly to the board due to traps existing. Explicitly
            adding the entity to the board requires overriding.
        '''
        random_x: int = random.randint(0, board._width-1)
        random_y: int = random.randint(0, board._height-1)
        self._position.set(random_x, random_y)
        
        while self._position in occupied_positions or board.at(self._position.x, self._position.y) != ' ':
            random_x = random.randint(0, board._width-1)
            random_y = random.randint(0, board._height-1)
            self._position.set(random_x, random_y)

        


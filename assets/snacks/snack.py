'''
    snack.py

    Parent class containing fields and methods that is shared across all types
    of snacks
'''
from typing import List
import random
from utils.consts import NORMAL_SNACK_POINTS
from utils.consts import SUPER_SNACK_POINTS
from utils.consts import NEW_SNACKS_START_LVL
from boards.board import Board
from assets.position.position2d import Position2D
from assets.enums.enums import SnackTypes
from assets.spawnable.spawnable import Spawnable

class Snack(Spawnable):
    _position: Position2D = Position2D()
    _count: int = 0
    _type: str = ''
    
    def spawn_snack(self, board: Board, occupied_positions: List[Position2D]) -> None:
        '''
            spawns snack on the grid

            Args:
                board: The board where the snack will be spawned.
        '''
        random_x: int = random.randint(0, board._width-1)
        random_y: int = random.randint(0, board._height-1)
        self._position.set(random_x, random_y)
        
        while self._position in occupied_positions or board.at(self._position.x, self._position.y) != ' ':
            print("looping")
            random_x = random.randint(0, board._width-1)
            random_y = random.randint(0, board._height-1)
            self._position.set(random_x, random_y)
        
        board.set(self._position.x, self._position.y, self._entity)

    def spawn(self, board: Board, occupied_positions: List[Position2D] = []) -> None:
        super().spawn(board, occupied_positions)
        board.set(self._position.x, self._position.y, self._entity)
    
    def clear_data(self) -> None:
        '''
            Clears snack data
        '''
        self._position.clear()
        self._count = 0

    def eat_snack(self, current_lvl_index: int, target_snack: Snack) -> None:
        '''
            Handles eating snack based on whether the player have reached
            a minimum level for newer snacks or not
        '''
        print("Eating snack...")
        if current_lvl_index >= NEW_SNACKS_START_LVL-1:
            match target_snack._type:
                case SnackTypes.NORMAL.value: self._count += NORMAL_SNACK_POINTS
                case SnackTypes.SUPER.value: self._count += SUPER_SNACK_POINTS
            self._position.clear()
        else:
            print("Sanck eaten!")
            self._count += NORMAL_SNACK_POINTS
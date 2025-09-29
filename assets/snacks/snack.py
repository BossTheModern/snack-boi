'''
    snack.py

    Parent class containing fields and methods that is shared across all types
    of snacks
'''
from typing import List
import random
import snack
from utils.consts import NORMAL_SNACK_POINTS
from utils.consts import SUPER_SNACK_POINTS
from utils.consts import NEW_SNACKS_START_LVL

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
    
    def clear_data(self) -> None:
        '''
            Clears snack data
        '''
        self._position.clear()
        self._count = 0

    def eat_snack(self, current_lvl_index: int, target_snack: snack) -> None:
        '''
            Handles eating snack based on whether the player have reached
            a minimum level for newer snacks or not
        '''
        print("Eating snack...")
        if current_lvl_index >= NEW_SNACKS_START_LVL-1:
            match target_snack._type:
                case 'normal': self._count += NORMAL_SNACK_POINTS
                case 'super': self._count += SUPER_SNACK_POINTS
            self._position.clear()
        else:
            print("Sanck eaten!")
            self._count += NORMAL_SNACK_POINTS
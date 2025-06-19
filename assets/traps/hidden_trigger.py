'''
    hidden_trigger.py

    handles logic for spawning hidden trigger on the parallel dimension
'''
from typing import List
import random

class HiddenTrigger:
    def __init__(self) -> None:
        self._position: List[int] = [0, 0]
        self._entity_char: str = 'T'
    
    def spawn(self, board: List[List[str]]) -> None:
        '''
            Spawns the hidden trigger on the parallel dimension
        '''
        self._position = [random.randint(0, len(board)-1), random.randint(0, len(board)-1)]
        while board[self._position[0]][self._position[1]] != ' ':
            self._position = [random.randint(0, len(board)-1), random.randint(0, len(board)-1)]
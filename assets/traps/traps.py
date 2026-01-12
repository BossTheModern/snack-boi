'''
    traps.py

    Parent class containing methods that is shared across all traps
'''
from typing import List
import random

class Trap:
    revealed: bool = False

    def spawn_trap(self, board: List[List[str]], occupied_positions: List[List[int]]) -> None:
        '''
            Spawns a trap on the board at a random available position. The
            traps are hidden by default
            Args:
                board: The board where the trap will be spawned.
        '''
        self._position = [random.randint(0, len(board)-1), random.randint(0, len(board)-1)]

        while self._position in occupied_positions or board[self._position[0]][self._position[1]] != ' ':
            self._position = [random.randint(0, len(board)-1), random.randint(0, len(board)-1)] 

        if self.revealed:
            board[self._position[0]][self._position[1]] = self._trap_entity   
    
    def reveal_trap(self, board: List[List[str]]) -> None:
        board[self._position[0]][self._position[1]] = self._trap_entity
        self.revealed = True
    
    def hide(self, board: List[List[str]]) -> None:
        board[self._position[0]][self._position[1]] = ' '
        self.revealed = False
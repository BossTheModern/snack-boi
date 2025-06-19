'''
    level.py

    Blueprint of individual levels
'''
from typing import List

class Level:
    _level_name: str
    _level_board: List[List[str]]
    _unlocked: bool
    _selected: bool
    _cleared: bool
    _win_cap: int

    def __init__(self, level_name: str, level_board: List[List[str]], 
                 unlocked: bool, selected: bool, cleared: bool, 
                 win_cap: int) -> None:
        self._level_name = level_name
        self._level_board = level_board
        self._unlocked = unlocked
        self._selected = selected
        self._cleared = cleared
        self._win_cap = win_cap
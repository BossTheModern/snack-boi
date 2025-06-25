'''
    levels.py

    A colection of all levels in the game
'''
import os
import sys
from typing import List
from assets.levels.level import Level

current_dir: str = os.path.dirname(os.path.abspath(__file__))
parent_dir: str = os.path.dirname(current_dir)
boards_dir: str = os.path.join(parent_dir, 'boards')

sys.path.insert(0, boards_dir)

from boards.grid_collection import square_obstacle_grid, square_obstacle_grid_2
from boards.grid_collection import square_obstacle_grid_3, square_obstacle_grid_4
from boards.grid_collection import square_obstacle_grid_5, square_obstacle_grid_6
from boards.grid_collection import square_obstacle_grid_7, square_obstacle_grid_8
from boards.grid_collection import square_obstacle_grid_9, square_obstacle_grid_10
from boards.grid_collection import square_obstacle_grid_11, square_obstacle_grid_12
from boards.grid_collection import square_obstacle_grid_13, square_obstacle_grid_14
from boards.grid_collection import square_obstacle_grid_15


class Levels:
    '''
        Levels class storing all levels in the game
        
        Level win cap setup:
            lvl 1 - 4: 10
            lvl 5 - 7: 15
            lvl 8 - 10: 20
            lvl 11 - 15: 25
    '''
    _win_cap: int = 10
    _cap_increase_interval: int = 5
    _classic_levels_set_1: List[Level] = [Level("Level 1", square_obstacle_grid, True, True, False, _win_cap), 
                                          Level("Level 2", square_obstacle_grid_2, False, False, False, _win_cap),
                                          Level("Level 3", square_obstacle_grid_3, False, False, False, _win_cap),
                                          Level("Level 4", square_obstacle_grid_4, False, False, False, _win_cap),
                                          Level("Level 5", square_obstacle_grid_5, False, False, False, _win_cap + _cap_increase_interval),
                                          Level("Level 6", square_obstacle_grid_6, False, False, False, _win_cap + _cap_increase_interval),
                                          Level("Level 7", square_obstacle_grid_7, False, False, False, _win_cap + _cap_increase_interval),
                                          Level("Level 8", square_obstacle_grid_8, False, False, False, _win_cap + _cap_increase_interval * 2),
                                          Level("Level 9", square_obstacle_grid_9, False, False, False, _win_cap + _cap_increase_interval * 2),
                                          Level("Level 10", square_obstacle_grid_10, False, False, False, _win_cap + _cap_increase_interval * 2),
                                          Level("Level 11", square_obstacle_grid_11, False, False, False, _win_cap + _cap_increase_interval * 3),
                                          Level("Level 12", square_obstacle_grid_12, False, False, False, _win_cap + _cap_increase_interval * 3),
                                          Level("Level 13", square_obstacle_grid_13, False, False, False, _win_cap + _cap_increase_interval * 3),
                                          Level("Level 14", square_obstacle_grid_14, False, False, False, _win_cap + _cap_increase_interval * 3),
                                          Level("Level 15", square_obstacle_grid_15, False, False, False, _win_cap + _cap_increase_interval * 3),]
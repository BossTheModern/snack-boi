'''
    levels.py

    A colection of all levels in the game
'''
import os
import sys
from typing import List
from assets.levels.level import Level
from utils.consts import BASE_LEVEL_REWARD
from utils.consts import INTERMEDIATE_LEVEL_REWARD
from utils.consts import ADVANCED_LEVEL_REWARD
from assets.collection.collection import Collection

current_dir: str = os.path.dirname(os.path.abspath(__file__))
parent_dir: str = os.path.dirname(current_dir)
boards_dir: str = os.path.join(parent_dir, 'boards')

sys.path.insert(0, boards_dir)

class Levels(Collection):
    '''
        Levels class storing all levels in the game
        Rules for levels apply when instantiating the class with list of levels
        containing only board data
        
        Level win cap setup:
            lvl 1 - 4: 10
            lvl 5 - 7: 15
            lvl 8 - 10: 20
            lvl 11 - 15: 25
    '''
    def __init__(self, levels: List[Level] = []) -> None:
        super().__init__(levels, page_size = 15)
        self._win_cap: int = 10

        # algorithm properly setting up levels using level system rules
        for i, level in enumerate(self._items):
            self.sequential_level_naming(i, level)
            self.standard_unlock_select_rule(i, level)
            self.win_cap_increase_rule(i, level)
            self.reward_rules(i, level)

    def standard_unlock_select_rule(self, level_index: int, level: Level) -> None:
        if level_index+1 == 1:
            level._unlocked = True
            level._selected = True

    def sequential_level_naming(self, level_index: int, level: Level) -> None:
        level._level_name = "Level " + str(level_index+1)

    def win_cap_increase_rule(self, level_index: int, level: Level) -> None:
        if level_index+1 >= 11:
            level._win_cap = 25
        elif level_index+1 >= 8:
            level._win_cap = 20
        elif level_index+1 >= 5:
            level._win_cap = 15
        else:
            level._win_cap = self._win_cap

    def reward_rules(self, level_index: int, level: Level) -> None:
        if level_index+1 >= 10:
            level._reward = ADVANCED_LEVEL_REWARD
        elif level_index+1 >= 5:
            level._reward = INTERMEDIATE_LEVEL_REWARD
        else:
            level._reward = BASE_LEVEL_REWARD

    # Level blueprint
    # _levels: List[Level] = [Level("Level 1", square_obstacle_grid, True, True, False, _win_cap, BASE_LEVEL_REWARD), 
    #                         Level("Level 2", square_obstacle_grid_2, False, False, False, _win_cap, BASE_LEVEL_REWARD),
    #                         Level("Level 3", square_obstacle_grid_3, False, False, False, _win_cap, BASE_LEVEL_REWARD),
    #                         Level("Level 4", square_obstacle_grid_4, False, False, False, _win_cap, BASE_LEVEL_REWARD),
    #                         Level("Level 5", square_obstacle_grid_5, False, False, False, _win_cap + _cap_increase_interval, INTERMEDIATE_LEVEL_REWARD),
    #                         Level("Level 6", square_obstacle_grid_6, False, False, False, _win_cap + _cap_increase_interval, INTERMEDIATE_LEVEL_REWARD),
    #                         Level("Level 7", square_obstacle_grid_7, False, False, False, _win_cap + _cap_increase_interval, INTERMEDIATE_LEVEL_REWARD),
    #                         Level("Level 8", square_obstacle_grid_8, False, False, False, _win_cap + _cap_increase_interval * 2, INTERMEDIATE_LEVEL_REWARD),
    #                         Level("Level 9", square_obstacle_grid_9, False, False, False, _win_cap + _cap_increase_interval * 2, INTERMEDIATE_LEVEL_REWARD),
    #                         Level("Level 10", square_obstacle_grid_10, False, False, False, _win_cap + _cap_increase_interval * 2, ADVANCED_LEVEL_REWARD),
    #                         Level("Level 11", square_obstacle_grid_11, False, False, False, _win_cap + _cap_increase_interval * 3, ADVANCED_LEVEL_REWARD),
    #                         Level("Level 12", square_obstacle_grid_12, False, False, False, _win_cap + _cap_increase_interval * 3, ADVANCED_LEVEL_REWARD),
    #                         Level("Level 13", square_obstacle_grid_13, False, False, False, _win_cap + _cap_increase_interval * 3, ADVANCED_LEVEL_REWARD),
    #                         Level("Level 14", square_obstacle_grid_14, False, False, False, _win_cap + _cap_increase_interval * 3, ADVANCED_LEVEL_REWARD),
    #                         Level("Level 15", square_obstacle_grid_15, False, False, False, _win_cap + _cap_increase_interval * 3, ADVANCED_LEVEL_REWARD),
    #                         Level("Level 16", square_obstacle_grid_16, False, False, False, _win_cap + _cap_increase_interval * 3, ADVANCED_LEVEL_REWARD),
    #                         Level("Level 17", square_obstacle_grid_17, False, False, False, _win_cap + _cap_increase_interval * 3, ADVANCED_LEVEL_REWARD),
    #                         Level("Level 18", square_obstacle_grid_18, False, False, False, _win_cap + _cap_increase_interval * 3, ADVANCED_LEVEL_REWARD),
    #                         Level("Level 19", square_obstacle_grid_19, False, False, False, _win_cap + _cap_increase_interval * 3, ADVANCED_LEVEL_REWARD),
    #                         Level("Level 20", square_obstacle_grid_20, False, False, False, _win_cap + _cap_increase_interval * 3, ADVANCED_LEVEL_REWARD),]
'''
    consts.py

    Game related constants for game configs
'''
# game settings and configurations
HUNGER_TRAPS_LIMIT: int = 7
PARALLEL_TRAPS_LIMIT: int = 4
TRAP_START_LVL: int = 8
NEW_SNACKS_START_LVL: int = 5
SHOP_ITEM_LIMIT: int = 3
VERSION: str = "0.5.0 alpha"
VERSION_LOG_FILE_PATH: str = 'version_log.txt'
SAVE_FILE_PATH: str = 'assets/save_files/save_file.txt'

# Account configs
NAME_MIN_LENGTH: int = 1
NAME_MAX_LENGTH: int = 20
START_POINTS: int = 100

# points for eating snacks
NORMAL_SNACK_POINTS: int = 1
SUPER_SNACK_POINTS: int = 2

# level rewards
NORMAL_LVL_REWARD: int = 5
NEW_SNACK_LVL_REWARD: int = 10
TRAPPED_LVL_REWARD: int = 15
'''
    consts.py

    Game related constants for game configs
'''
from assets.shop.shop_item import ShopItem

# game settings and configurations
HUNGER_TRAPS_LIMIT: int = 7
PARALLEL_TRAPS_LIMIT: int = 4
TRAP_START_LVL: int = 8
NEW_SNACKS_START_LVL: int = 5
SHOP_ITEM_LIMIT: int = 3
VERSION: str = "0.6.0 alpha"
VERSION_LOG_FILE_PATH: str = 'version_log.txt'
SAVE_FILE_PATH: str = 'assets/save_files/save_file.txt'
STD_WIDTH: int = 10
STD_HEIGHT: int = 10

# Account configs
NAME_MIN_LENGTH: int = 1
NAME_MAX_LENGTH: int = 20
START_POINTS: int = 100

# file
END_OF_ITEMS_FLAG: str = "end_of_items"

# points for eating snacks
NORMAL_SNACK_POINTS: int = 1
SUPER_SNACK_POINTS: int = 2

# level rewards
BASE_LEVEL_REWARD: int = 5
INTERMEDIATE_LEVEL_REWARD: int = BASE_LEVEL_REWARD * 2
ADVANCED_LEVEL_REWARD: int = BASE_LEVEL_REWARD * 3

EMPTY_SHOP_ITEM: ShopItem = ShopItem("None", 0, "", 0)
PAGE_SIZE: int = 3
EMPTY_SPACE: str = ' '

PLAYER_ENTITY: str = 'O'
SNACK_ENTITY: str = '*'
SUPER_SNACK_ENTITY: str = '#'
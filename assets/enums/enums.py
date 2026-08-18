'''
    enums.py

    Custom enums function
'''
from enum import Enum

class MainMenuOptions(Enum):
    START_GAME = '1'
    SHOP_MENU = '2'
    ACCOUNT = '3'
    OPTIONS = '4'
    VERSION_LOG = '5'
    QUIT = '6'

class MovementKeys(Enum):
    UP = 'w'
    DOWN = 's'
    LEFT = 'a'
    RIGHT = 'd'

class ModeSelection(Enum):
    CLASSIC_MODE = '1'
    ENDLESS_MODE = '2'
    BACK = '3'

class OptionsSelection(Enum):
    MANAGE_SAVE_FILE = '1'
    BACK = '2'

class SaveFileOptions(Enum):
    LOAD_PROGRESS = '1'
    SAVE_PROGRESS = '2'
    DELETE_SAVE = '3'
    BACK = '4'

class Gamemodes(Enum):
    CLASSIC = 'classic'
    ENDLESS = 'endless'

class Confirmation(Enum):
    YES = 'y'
    NO = 'n'

class SnackTypes(Enum):
    NORMAL = 'normal'
    FAKE = 'fake'
    SUPER = 'super'

class AccountOptions(Enum):
    CHANGE_NAME = 'e'
    BACK = 'q'
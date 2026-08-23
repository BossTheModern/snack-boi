'''
    dimension_exit.py

    handles logic for spawning parallel dimension exit
'''
from assets.spawnable.spawnable import Spawnable

class DimensionExit(Spawnable):
    def __init__(self) -> None:
        super().__init__('E')

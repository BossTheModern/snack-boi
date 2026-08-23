'''
    dimension_exit.py

    handles logic for spawning parallel dimension exit
'''
from boards.board import Board
from assets.position.position2d import Position2D 
from assets.spawnable.spawnable import Spawnable

class DimensionExit(Spawnable):
    def __init__(self) -> None:
        super().__init__('E')

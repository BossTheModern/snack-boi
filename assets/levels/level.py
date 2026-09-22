'''
    level.py

    Blueprint of individual levels
'''
from boards.board import Board
from assets.teleport_pod.teleport_pods import TeleportPods
from assets.position.position2d import Position2D

class Level:
    _level_name: str
    _level_board: Board
    _unlocked: bool
    _selected: bool
    _cleared: bool
    _win_cap: int
    _reward: int
    _teleport_pods: TeleportPods | None

    def __init__(self,  level_board: Board, level_name: str = "", 
                 unlocked: bool = False, selected: bool = False, cleared: bool = False, 
                 win_cap: int = 0, reward: int = 0, teleport_pods: TeleportPods | None = None) -> None:
        self._level_name = level_name
        self._level_board = level_board
        self._unlocked = unlocked
        self._selected = selected
        self._cleared = cleared
        self._win_cap = win_cap
        self._reward = reward
        self._teleport_pods = teleport_pods
        self.set_teleport_pods()

    def set_teleport_pods(self) -> None:
        if self._teleport_pods == None:
            return

        for y, row in enumerate(self._level_board._board):
            for x, space in enumerate(row):
                if space == self._teleport_pods._entity:
                    self._teleport_pods.add_position(Position2D(x, y))
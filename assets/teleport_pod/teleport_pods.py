'''
    teleport_pod.py

    teleport pod used to teleport to enclosed spaces
'''
from assets.position.position2d import Position2D
from typing import List

class TeleportPods:
    def __init__(self) -> None:
        self._positions: List[Position2D] = []
        self._pods_limit: int = 2
        self._entity: str = 'T'
        self.maintain_limit()

    def maintain_limit(self) -> None:
        while len(self._positions) > self._pods_limit:
            self._positions.remove(self._positions[-1])

    def add_position(self, position: Position2D) -> None:
        if len(self._positions) == self._pods_limit:
            return
        
        self._positions.append(position)
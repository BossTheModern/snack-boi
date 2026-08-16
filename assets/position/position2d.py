'''
    position.py

    custom 2D position class with appropriate positional functions
'''
from collections.abc import Iterable

class Position2D:
    def __init__(self, x: int = -1, y: int = -1) -> None:
        self.x = x
        self.y = y

    def __eq__(self, other) -> bool:
        if not isinstance(other, Position2D):
            return False

        return self.x == other.x and self.y == other.y

    def is_in(self, items: Iterable) -> bool:
        item_found: bool = False

        for item in items:
            if self == item:
                item_found = True
                break

        return item_found

    def get(self) -> tuple[int, int]:
        return self.x, self.y

    def set(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def clear(self) -> None:
        self.x = -1
        self.y = -1

    def move_up(self, val: int = 1) -> None:
        self.y -= val

    def move_down(self, val: int = 1) -> None:
        self.y += val

    def move_left(self, val: int = 1) -> None:
        self.x -= val

    def move_right(self, val: int = 1) -> None:
        self.x += val
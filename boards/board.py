'''
    board.py

    class board containing width, height containing functions that
    can add obstacles to it
'''
from typing import List

class Board:
    def __init__(self, width: int, height: int) -> None:
        self._width: int = abs(width)
        self._height: int = abs(height)
        self._board: List[List[str]] = [[' ' for _ in range(width)] for _ in range(height)]

    def at(self, col: int, row: int) -> str:
        return self._board[row][col]

    def set(self, col: int, row: int, obj: str) -> None:
        self._board[row][col] = obj

    def display(self) -> None:
        '''
            Draws a grid using the grid data container using tile data for 
            each tile
        '''

        def border_line() -> None:
            '''
                Draws a border line with specified pattern with specified length:
                Example of border line with length = 5
                |---|---|---|---|---|
            '''
            print("|", end="")
            for _ in range(self._width):
                print('---|', end="")
            print()

        border_line()
        
        for row in self._board:
            print("|", end="")
            for tile in row:
                print("", tile, "|", end="")
            print()
            border_line()
        print()

    def is_within_bounds(self, row: int, col: int) -> bool:
        return 1 <= row <= self._height and 1 <= col <= self._width

    def add_obstacles_vertically(self, row: int, col: int, length: int, char: str) -> None:
        '''
            adds obstacles vertically starting from a set point on the board
            to a set length
        '''
        if not self.is_within_bounds(row, col):
            return
    
        for i in range(length):
            if row-1 + i > len(self._board)-1:
                return
            self._board[row-1 + i][col-1] = char

    def add_obstacles_horizontally(self, row: int, col: int, length: int, char: str) -> None:
        '''
            adds obstacles horizontally starting from a set point on the board
            to a set length
        '''
        if not self.is_within_bounds(row, col):
            return 

        for i in range(length):
            if col-1 + i > len(self._board[0]) - 1:
                return
            self._board[row-1][col-1 + i] = char

    def add_obstacle(self, row: int, col: int, char: str) -> None:
        '''
            Adds an obstacle to the specified position on the board
        '''
        if not self.is_within_bounds(row, col):
            return
        self._board[row-1][col-1] = char

    def empty(self) -> bool:
        return self._height == 0 and self._width == 0
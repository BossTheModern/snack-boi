'''
    board_creator.py

    Toolbox with drawing tools to create grids with obstacles 
'''
from typing import List

OBSTACLE_CHAR: str = 'X'

grid_void: List[List[str]] = [[' ' for _ in range(10)] for _ in range(10)]
rectangular_grid_void: List[List[str]] = [[' ' for _ in range(5)] for _ in range(3)]
rectangular_grid_void_2: List[List[str]] = [[' ' for _ in range(3)] for _ in range(5)]

def border_line(length: int) -> None:
    '''
        Draws a border line with specified pattern with specified length:
        Example of border line with length = 5
        |---|---|---|---|---|
    '''
    print("|", end="")
    for _ in range(length):
        print('---|', end="")
    print()

def draw_grid(grid: List[List[str]]) -> None:
    '''
        Draws a grid using the grid data container using tile data for 
        each tile
    '''
    border_line(len(grid[0]))
    for row in grid:
        print("|", end="")
        for tile in row:
            print("", tile, "|", end="")
        print()
        border_line(len(grid[0]))
    print()

def preview_grid(grid: List[List[str]], name: str) -> None:
    print(f"Preview of the grid {name}:")
    draw_grid(grid)

def is_within_bounds(grid: List[List[str]], row: int, col: int) -> bool:
    return 0 <= row < len(grid) and 0 <= col < len(grid[0])

# Obstacle functions
def add_obstacles_vertically(grid: List[List[str]], row: int, col: int, length: int, char: str) -> None:
    '''
        adds obstacles vertically starting from a set point on the board
        to a set length
    '''
    if not is_within_bounds(grid, row-1, col-1):
        return
    
    for i in range(length):
        if row-1 + i > len(grid)-1:
            return
        grid[row-1 + i][col-1] = char

def add_obstacles_horizontally(grid: List[List[str]], row: int, col: int, length: int, char: str) -> None:
    '''
        adds obstacles horizontally starting from a set point on the board
        to a set length
    '''
    if not is_within_bounds(grid, row-1, col-1):
        return 

    for i in range(length):
        if col-1 + i > len(grid[0]) - 1:
            return
        grid[row-1][col-1 + i] = char

def add_obstacle(grid: List[List[str]], row: int, col: int, char: str) -> None:
    '''
        Adds an obstacle to the specified position on the board
    '''
    if not is_within_bounds(grid, row-1, col-1):
        return
    grid[row-1][col-1] = char
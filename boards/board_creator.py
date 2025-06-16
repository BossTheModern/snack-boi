# Module including functions related to drawing and editing boards
from typing import List

obstacle_char: str = 'X'

grid_void: List[List[str]] = [[' ' for _ in range(10)] for _ in range(10)]
rectangular_grid_void: List[List[str]] = [[' ' for _ in range(5)] for _ in range(3)]
rectangular_grid_void_2: List[List[str]] = [[' ' for _ in range(3)] for _ in range(5)]

def border_line(length: int) -> None:
    print("|", end="")
    for _ in range(length):
        print('---|', end="")
    print()

def draw_grid(grid: List[List[str]]) -> None:
    border_line(len(grid[0]))
    for row in grid:
        print("|", end="")
        for tile in row:
            print("", tile, "|", end="")
        print()
        border_line(len(grid[0]))
    print()

def preview_grid(grid: List[List[str]], name: str) -> None:
    print("Preview of the grid,", name + ":")
    draw_grid(grid)

# Obstacle functions
# These functions are used to add obstacles to the grid.
def is_within_bounds(grid: List[List[str]], row: int, col: int) -> bool:
    return 0 <= row < len(grid) and 0 <= col < len(grid[0])

def add_obstacles_vertically(grid: List[List[str]], row: int, col: int, length: int, char: str) -> None:
    if not is_within_bounds(grid, row-1, col-1):
        return
    
    for i in range(length):
        if row-1 + i > len(grid)-1:
            return
        grid[row-1 + i][col-1] = char

def add_obstacles_horizontally(grid: List[List[str]], row: int, col: int, length: int, char: str) -> None:
    if not is_within_bounds(grid, row-1, col-1):
        return 

    for i in range(length):
        if col-1 + i > len(grid[0]) - 1:
            return
        grid[row-1][col-1 + i] = char

def add_obstacle(grid: List[List[str]], row: int, col: int, char: str) -> None:
    if not is_within_bounds(grid, row-1, col-1):
        return
    grid[row-1][col-1] = char
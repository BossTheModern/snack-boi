from board_creator import draw_grid
from grid_collection import square_obstacle_grid
from typing import List

if __name__ == "__main__":
    # Ask for input for grid size
    grid_width : int = int(input("Enter grid width: "))
    grid_height : int = int(input("Enter grid height: "))

    # Create a grid with specified size
    grid : List[List[str]] = [[' ' for _ in range(grid_width)] for _ in range(grid_height)]
    draw_grid(grid)
    draw_grid(square_obstacle_grid)
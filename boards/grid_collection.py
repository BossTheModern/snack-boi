'''
grid_collection.py

This module provides a collection of grids to use for levels
All grids are of size 10x10 
All grids have obstacles except for the square_grid
To preview the grid, toggle the commenting on the preview_grid function.
Additionally, some can include obstacles, which are represented by a specific character.
It includes methods to load grid files, save grid files, and display the contents of a grid file.
'''

from boards.board_creator import OBSTACLE_CHAR
from utils.consts import STD_HEIGHT, STD_WIDTH
from boards.board import Board

# Grids without obstacles
empty_grid: Board = Board(STD_WIDTH, STD_HEIGHT)


# Grids with obstacles
square_obstacle_grid: Board = Board(STD_WIDTH, STD_HEIGHT)

square_obstacle_grid.add_obstacles_horizontally(1, 8, 3, OBSTACLE_CHAR)
square_obstacle_grid.add_obstacles_horizontally(3, 1, 4, OBSTACLE_CHAR)
square_obstacle_grid.add_obstacles_horizontally(6, 7, 5, OBSTACLE_CHAR)
square_obstacle_grid.add_obstacles_vertically(1, 7, 4, OBSTACLE_CHAR)
square_obstacle_grid.add_obstacle(2, 4, OBSTACLE_CHAR)
square_obstacle_grid.add_obstacles_horizontally(8, 1, 5, OBSTACLE_CHAR)
square_obstacle_grid.add_obstacles_vertically(5, 4, 3, OBSTACLE_CHAR)
square_obstacle_grid.add_obstacle(10, 4, OBSTACLE_CHAR)


square_obstacle_grid_2: Board = Board(STD_WIDTH, STD_HEIGHT)

square_obstacle_grid_2.add_obstacles_horizontally(2, 2, 3, OBSTACLE_CHAR)
square_obstacle_grid_2.add_obstacles_horizontally(2, 7, 3, OBSTACLE_CHAR)
square_obstacle_grid_2.add_obstacles_vertically(2, 2, 3, OBSTACLE_CHAR)
square_obstacle_grid_2.add_obstacles_vertically(2, 4, 3, OBSTACLE_CHAR)
square_obstacle_grid_2.add_obstacles_vertically(2, 7, 3, OBSTACLE_CHAR)
square_obstacle_grid_2.add_obstacles_vertically(2, 9, 3, OBSTACLE_CHAR)

square_obstacle_grid_2.add_obstacles_horizontally(7, 2, 3, OBSTACLE_CHAR)
square_obstacle_grid_2.add_obstacles_horizontally(7, 7, 3, OBSTACLE_CHAR)
square_obstacle_grid_2.add_obstacles_vertically(7, 2, 3, OBSTACLE_CHAR)
square_obstacle_grid_2.add_obstacles_vertically(7, 4, 3, OBSTACLE_CHAR)
square_obstacle_grid_2.add_obstacles_vertically(7, 7, 3, OBSTACLE_CHAR)
square_obstacle_grid_2.add_obstacles_vertically(7, 9, 3, OBSTACLE_CHAR)


square_obstacle_grid_3: Board = Board(STD_WIDTH, STD_HEIGHT)

square_obstacle_grid_3.add_obstacles_horizontally(2, 1, 5, OBSTACLE_CHAR)
square_obstacle_grid_3.add_obstacles_vertically(2, 5, 3, OBSTACLE_CHAR)
square_obstacle_grid_3.add_obstacles_horizontally(4, 4, 2, OBSTACLE_CHAR)
square_obstacle_grid_3.add_obstacles_horizontally(6, 7, 4, OBSTACLE_CHAR)
square_obstacle_grid_3.add_obstacles_vertically(6, 8, 3, OBSTACLE_CHAR)
square_obstacle_grid_3.add_obstacles_horizontally(8, 1, 4, OBSTACLE_CHAR)
square_obstacle_grid_3.add_obstacles_vertically(6, 3, 2, OBSTACLE_CHAR)
square_obstacle_grid_3.add_obstacles_vertically(8, 4, 2, OBSTACLE_CHAR)
square_obstacle_grid_3.add_obstacles_vertically(1, 8, 3, OBSTACLE_CHAR)


square_obstacle_grid_4: Board = Board(STD_WIDTH, STD_HEIGHT)

square_obstacle_grid_4.add_obstacles_horizontally(1, 1, 5, OBSTACLE_CHAR)
square_obstacle_grid_4.add_obstacles_vertically(1, 5, 4, OBSTACLE_CHAR)
square_obstacle_grid_4.add_obstacles_horizontally(3, 8, 3, OBSTACLE_CHAR)
square_obstacle_grid_4.add_obstacles_vertically(3, 8, 6, OBSTACLE_CHAR)
square_obstacle_grid_4.add_obstacles_horizontally(6, 4, 4, OBSTACLE_CHAR)
square_obstacle_grid_4.add_obstacles_horizontally(9, 1, 5, OBSTACLE_CHAR)


square_obstacle_grid_5: Board = Board(STD_WIDTH, STD_HEIGHT)

square_obstacle_grid_5.add_obstacles_horizontally(2, 3, 6, OBSTACLE_CHAR)
square_obstacle_grid_5.add_obstacles_vertically(2, 8, 4, OBSTACLE_CHAR)
square_obstacle_grid_5.add_obstacles_vertically(2, 3, 7, OBSTACLE_CHAR)
square_obstacle_grid_5.add_obstacles_horizontally(8, 3, 3, OBSTACLE_CHAR)
square_obstacle_grid_5.add_obstacles_horizontally(5, 6, 2, OBSTACLE_CHAR)
square_obstacle_grid_5.add_obstacles_horizontally(7, 8, 3, OBSTACLE_CHAR)
square_obstacle_grid_5.add_obstacles_vertically(7, 8, 3, OBSTACLE_CHAR)


square_obstacle_grid_6: Board = Board(STD_WIDTH, STD_HEIGHT)

square_obstacle_grid_6.add_obstacles_vertically(1, 3, 5, OBSTACLE_CHAR)
square_obstacle_grid_6.add_obstacles_horizontally(5, 3, 4, OBSTACLE_CHAR)
square_obstacle_grid_6.add_obstacles_horizontally(8, 1, 6, OBSTACLE_CHAR)
square_obstacle_grid_6.add_obstacles_vertically(1, 7, 2, OBSTACLE_CHAR)
square_obstacle_grid_6.add_obstacles_horizontally(8, 9, 2, OBSTACLE_CHAR)


square_obstacle_grid_7: Board = Board(STD_WIDTH, STD_HEIGHT)

square_obstacle_grid_7.add_obstacles_vertically(1, 3, 4, OBSTACLE_CHAR)
square_obstacle_grid_7.add_obstacles_horizontally(3, 3, 5, OBSTACLE_CHAR)
square_obstacle_grid_7.add_obstacles_horizontally(6, 1, 5, OBSTACLE_CHAR)
square_obstacle_grid_7.add_obstacles_horizontally(6, 8, 3, OBSTACLE_CHAR)
square_obstacle_grid_7.add_obstacles_horizontally(8, 3, 3, OBSTACLE_CHAR)
square_obstacle_grid_7.add_obstacles_vertically(5, 5, 4, OBSTACLE_CHAR)
square_obstacle_grid_7.add_obstacles_vertically(6, 9, 4, OBSTACLE_CHAR)
square_obstacle_grid_7.add_obstacles_vertically(2, 7, 3, OBSTACLE_CHAR)


square_obstacle_grid_8: Board = Board(STD_WIDTH, STD_HEIGHT)

square_obstacle_grid_8.add_obstacles_vertically(1, 3, 4, OBSTACLE_CHAR)
square_obstacle_grid_8.add_obstacles_vertically(8, 2, 3, OBSTACLE_CHAR)
square_obstacle_grid_8.add_obstacles_vertically(6, 8, 4, OBSTACLE_CHAR)
square_obstacle_grid_8.add_obstacles_vertically(1, 8, 3, OBSTACLE_CHAR)
square_obstacle_grid_8.add_obstacles_horizontally(4, 2, 5, OBSTACLE_CHAR)
square_obstacle_grid_8.add_obstacles_horizontally(8, 2, 7, OBSTACLE_CHAR)
square_obstacle_grid_8.add_obstacles_horizontally(6, 2, 6, OBSTACLE_CHAR)
square_obstacle_grid_8.add_obstacles_horizontally(3, 8, 2, OBSTACLE_CHAR)


square_obstacle_grid_9: Board = Board(STD_WIDTH, STD_HEIGHT)

square_obstacle_grid_9.add_obstacles_horizontally(1, 2, 5, OBSTACLE_CHAR)
square_obstacle_grid_9.add_obstacles_horizontally(4, 2, 5, OBSTACLE_CHAR)
square_obstacle_grid_9.add_obstacles_horizontally(6, 2, 6, OBSTACLE_CHAR)
square_obstacle_grid_9.add_obstacles_horizontally(8, 3, 4, OBSTACLE_CHAR)
square_obstacle_grid_9.add_obstacles_horizontally(10, 1, 5, OBSTACLE_CHAR)
square_obstacle_grid_9.add_obstacles_vertically(2, 2, 3, OBSTACLE_CHAR)
square_obstacle_grid_9.add_obstacles_vertically(1, 9, 6, OBSTACLE_CHAR)
square_obstacle_grid_9.add_obstacles_vertically(6, 7, 3, OBSTACLE_CHAR)
square_obstacle_grid_9.add_obstacles_vertically(9, 1, 2, OBSTACLE_CHAR)
square_obstacle_grid_9.add_obstacles_vertically(9, 9, 3, OBSTACLE_CHAR)


square_obstacle_grid_10: Board = Board(STD_WIDTH, STD_HEIGHT)

square_obstacle_grid_10.add_obstacles_horizontally(2, 4, 4, OBSTACLE_CHAR)
square_obstacle_grid_10.add_obstacles_horizontally(5, 4, 4, OBSTACLE_CHAR)
square_obstacle_grid_10.add_obstacles_horizontally(7, 2, 8, OBSTACLE_CHAR)
square_obstacle_grid_10.add_obstacles_horizontally(9, 2, 5, OBSTACLE_CHAR)
square_obstacle_grid_10.add_obstacles_horizontally(4, 1, 3, OBSTACLE_CHAR)
square_obstacle_grid_10.add_obstacles_vertically(2, 4, 4, OBSTACLE_CHAR)
square_obstacle_grid_10.add_obstacles_vertically(3, 9, 8, OBSTACLE_CHAR)
square_obstacle_grid_10.add_obstacles_vertically(7, 4, 3, OBSTACLE_CHAR)
square_obstacle_grid_10.add_obstacles_vertically(1, 1, 4, OBSTACLE_CHAR)


square_obstacle_grid_11: Board = Board(STD_WIDTH, STD_HEIGHT)

square_obstacle_grid_11.add_obstacles_vertically(1, 4, 4, OBSTACLE_CHAR)
square_obstacle_grid_11.add_obstacles_vertically(5, 6, 4, OBSTACLE_CHAR)
square_obstacle_grid_11.add_obstacles_vertically(6, 9, 4, OBSTACLE_CHAR)
square_obstacle_grid_11.add_obstacles_vertically(1, 7, 2, OBSTACLE_CHAR)
square_obstacle_grid_11.add_obstacles_horizontally(4, 3, 7, OBSTACLE_CHAR)
square_obstacle_grid_11.add_obstacles_horizontally(7, 1, 3, OBSTACLE_CHAR)
square_obstacle_grid_11.add_obstacles_horizontally(2, 1, 2, OBSTACLE_CHAR)
square_obstacle_grid_11.add_obstacle(9, 8, OBSTACLE_CHAR)


square_obstacle_grid_12: Board = Board(STD_WIDTH, STD_HEIGHT)

square_obstacle_grid_12.add_obstacles_horizontally(2, 2, 5, OBSTACLE_CHAR)
square_obstacle_grid_12.add_obstacles_horizontally(4, 3, 6, OBSTACLE_CHAR)
square_obstacle_grid_12.add_obstacles_horizontally(7, 2, 6, OBSTACLE_CHAR)
square_obstacle_grid_12.add_obstacles_horizontally(9, 3, 6, OBSTACLE_CHAR)
square_obstacle_grid_12.add_obstacles_horizontally(8, 5, 2, OBSTACLE_CHAR)
square_obstacle_grid_12.add_obstacles_horizontally(5, 6, 4, OBSTACLE_CHAR)
square_obstacle_grid_12.add_obstacle(3, 7, OBSTACLE_CHAR)



square_obstacle_grid_13: Board = Board(STD_WIDTH, STD_HEIGHT)

square_obstacle_grid_13.add_obstacles_horizontally(2, 2, 4, OBSTACLE_CHAR)
square_obstacle_grid_13.add_obstacles_horizontally(3, 4, 4, OBSTACLE_CHAR)
square_obstacle_grid_13.add_obstacles_horizontally(4, 5, 4, OBSTACLE_CHAR)
square_obstacle_grid_13.add_obstacles_horizontally(8, 2, 4, OBSTACLE_CHAR)
square_obstacle_grid_13.add_obstacles_horizontally(7, 5, 4, OBSTACLE_CHAR)
square_obstacle_grid_13.add_obstacle(6, 9, OBSTACLE_CHAR)
square_obstacle_grid_13.add_obstacle(9, 8, OBSTACLE_CHAR)
square_obstacle_grid_13.add_obstacle(10, 7, OBSTACLE_CHAR)


square_obstacle_grid_14: Board = Board(STD_WIDTH, STD_HEIGHT)

square_obstacle_grid_14.add_obstacles_vertically(6, 4, 4, OBSTACLE_CHAR)
square_obstacle_grid_14.add_obstacles_horizontally(2, 2, 4, OBSTACLE_CHAR)
square_obstacle_grid_14.add_obstacles_horizontally(3, 5, 4, OBSTACLE_CHAR)
square_obstacle_grid_14.add_obstacles_horizontally(5, 3, 4, OBSTACLE_CHAR)
square_obstacle_grid_14.add_obstacles_horizontally(8, 7, 3, OBSTACLE_CHAR)
square_obstacle_grid_14.add_obstacles_horizontally(8, 1, 3, OBSTACLE_CHAR)
square_obstacle_grid_14.add_obstacle(7, 10, OBSTACLE_CHAR)
square_obstacle_grid_14.add_obstacle(4, 9, OBSTACLE_CHAR)


square_obstacle_grid_15: Board = Board(STD_WIDTH, STD_HEIGHT)

square_obstacle_grid_15.add_obstacles_vertically(3, 9, 4, OBSTACLE_CHAR)
square_obstacle_grid_15.add_obstacles_vertically(5, 2, 4, OBSTACLE_CHAR)
square_obstacle_grid_15.add_obstacles_horizontally(2, 5, 5, OBSTACLE_CHAR)
square_obstacle_grid_15.add_obstacles_horizontally(9, 2, 5, OBSTACLE_CHAR)
square_obstacle_grid_15.add_obstacles_horizontally(5, 5, 2, OBSTACLE_CHAR)
square_obstacle_grid_15.add_obstacles_horizontally(6, 5, 2, OBSTACLE_CHAR)
square_obstacle_grid_15.add_obstacles_horizontally(2, 2, 2, OBSTACLE_CHAR)
square_obstacle_grid_15.add_obstacles_horizontally(9, 8, 2, OBSTACLE_CHAR)
square_obstacle_grid_15.add_obstacle(3, 2, OBSTACLE_CHAR)
square_obstacle_grid_15.add_obstacle(8, 9, OBSTACLE_CHAR)

square_obstacle_grid_16: Board = Board(STD_WIDTH, STD_HEIGHT)

square_obstacle_grid_16.add_obstacles_horizontally(2, 3, 6, OBSTACLE_CHAR)
square_obstacle_grid_16.add_obstacle(3, 2, OBSTACLE_CHAR)
square_obstacle_grid_16.add_obstacle(3, 9, OBSTACLE_CHAR)
square_obstacle_grid_16.add_obstacles_horizontally(6, 2, 3, OBSTACLE_CHAR)
square_obstacle_grid_16.add_obstacles_horizontally(6, 7, 3, OBSTACLE_CHAR)
square_obstacle_grid_16.add_obstacles_vertically(9, 4, 2, OBSTACLE_CHAR)
square_obstacle_grid_16.add_obstacles_vertically(9, 7, 2, OBSTACLE_CHAR)



square_obstacle_grid_17: Board = Board(STD_WIDTH, STD_HEIGHT)

square_obstacle_grid_17.add_obstacles_horizontally(2, 6, 4, OBSTACLE_CHAR)
square_obstacle_grid_17.add_obstacles_horizontally(3, 4, 2, OBSTACLE_CHAR)
square_obstacle_grid_17.add_obstacles_horizontally(4, 2, 2, OBSTACLE_CHAR)
square_obstacle_grid_17.add_obstacles_horizontally(6, 6, 4, OBSTACLE_CHAR)
square_obstacle_grid_17.add_obstacles_horizontally(7, 4, 2, OBSTACLE_CHAR)
square_obstacle_grid_17.add_obstacles_horizontally(8, 2, 2, OBSTACLE_CHAR)
square_obstacle_grid_17.add_obstacles_vertically(8, 9, 3, OBSTACLE_CHAR)
square_obstacle_grid_17.add_obstacles_horizontally(9, 5, 4, OBSTACLE_CHAR)


square_obstacle_grid_18: Board = Board(STD_WIDTH, STD_HEIGHT)

square_obstacle_grid_18.add_obstacles_horizontally(5, 1, 4, OBSTACLE_CHAR)
square_obstacle_grid_18.add_obstacles_vertically(1, 7, 3, OBSTACLE_CHAR)
square_obstacle_grid_18.add_obstacles_vertically(1, 3, 3, OBSTACLE_CHAR)
square_obstacle_grid_18.add_obstacles_horizontally(3, 8, 2, OBSTACLE_CHAR)
square_obstacle_grid_18.add_obstacles_horizontally(5, 6, 5, OBSTACLE_CHAR)
square_obstacle_grid_18.add_obstacles_horizontally(7, 1, 7, OBSTACLE_CHAR)
square_obstacle_grid_18.add_obstacles_horizontally(9, 6, 5, OBSTACLE_CHAR)
square_obstacle_grid_18.add_obstacles_vertically(8, 3, 2, OBSTACLE_CHAR)

square_obstacle_grid_19: Board = Board(STD_WIDTH, STD_HEIGHT)

square_obstacle_grid_19.add_obstacles_horizontally(2, 1, 5, OBSTACLE_CHAR)
square_obstacle_grid_19.add_obstacles_horizontally(4, 2, 5, OBSTACLE_CHAR)
square_obstacle_grid_19.add_obstacles_horizontally(6, 5, 2, OBSTACLE_CHAR)
square_obstacle_grid_19.add_obstacles_vertically(1, 7, 4, OBSTACLE_CHAR)
square_obstacle_grid_19.add_obstacles_vertically(6, 3, 3, OBSTACLE_CHAR)
square_obstacle_grid_19.add_obstacles_vertically(6, 3, 3, OBSTACLE_CHAR)
square_obstacle_grid_19.add_obstacles_vertically(4, 8, 3, OBSTACLE_CHAR)
square_obstacle_grid_19.add_obstacles_vertically(6, 1, 4, OBSTACLE_CHAR)
square_obstacle_grid_19.add_obstacles_vertically(1, 10, 5, OBSTACLE_CHAR)
square_obstacle_grid_19.add_obstacles_vertically(7, 10, 4, OBSTACLE_CHAR)
square_obstacle_grid_19.add_obstacles_horizontally(8, 4, 3, OBSTACLE_CHAR)
square_obstacle_grid_19.add_obstacles_horizontally(10, 1, 5, OBSTACLE_CHAR)


square_obstacle_grid_20: Board = Board(STD_WIDTH, STD_HEIGHT)

square_obstacle_grid_20.add_obstacles_horizontally(8, 3, 4, OBSTACLE_CHAR)
square_obstacle_grid_20.add_obstacles_horizontally(6, 4, 5, OBSTACLE_CHAR)
square_obstacle_grid_20.add_obstacles_horizontally(4, 1, 6, OBSTACLE_CHAR)
square_obstacle_grid_20.add_obstacles_horizontally(2, 4, 4, OBSTACLE_CHAR)
square_obstacle_grid_20.add_obstacles_horizontally(4, 1, 6, OBSTACLE_CHAR)
square_obstacle_grid_20.add_obstacles_vertically(6, 9, 5, OBSTACLE_CHAR)
square_obstacle_grid_20.add_obstacles_vertically(1, 2, 2, OBSTACLE_CHAR)
square_obstacle_grid_20.add_obstacles_vertically(2, 8, 3, OBSTACLE_CHAR)
square_obstacle_grid_20.add_obstacles_vertically(1, 10, 4, OBSTACLE_CHAR)
square_obstacle_grid_20.add_obstacle(9, 2, OBSTACLE_CHAR)
square_obstacle_grid_20.add_obstacle(10, 1, OBSTACLE_CHAR)
square_obstacle_grid_20.add_obstacle(4, 9, OBSTACLE_CHAR)

'''
-----grid_collection.py-----
This module provides a collection of grid files.
All grids are of size 10x10 
All grids have obstacls except for the square_grid
To preview the grid, toggle the commenting on the preview_grid function.
Additionally, some can include obstacles, which are represented by a specific character.
It includes methods to load grid files, save grid files, and display the contents of a grid file.
'''

from board_creator import add_obstacles_horizontally, add_obstacles_vertically
from board_creator import add_obstacle, obstacle_char, preview_grid
from typing import List


# Grids without obstacles
empty_grid: List[List[str]] = [[' ' for _ in range(10)] for _ in range(10)]
#preview_grid(square_grid, "square_grid")


# Grids with obstacles
square_obstacle_grid: List[List[str]] = [[' ' for _ in range(10)] for _ in range(10)]

add_obstacles_horizontally(square_obstacle_grid, 1, 8, 3, obstacle_char)
add_obstacles_horizontally(square_obstacle_grid, 3, 1, 4, obstacle_char)
add_obstacles_horizontally(square_obstacle_grid, 6, 7, 5, obstacle_char)
add_obstacles_vertically(square_obstacle_grid, 1, 7, 4, obstacle_char)
add_obstacle(square_obstacle_grid, 2, 4, obstacle_char)
add_obstacles_horizontally(square_obstacle_grid, 8, 1, 5, obstacle_char)
add_obstacles_vertically(square_obstacle_grid, 5, 4, 3, obstacle_char)
add_obstacle(square_obstacle_grid, 10, 4, obstacle_char)

#preview_grid(square_obstacle_grid, "square_obstacle_grid")

square_obstacle_grid_2: List[List[str]] = [[' ' for _ in range(10)] for _ in range(10)]

add_obstacles_horizontally(square_obstacle_grid_2, 2, 2, 3, obstacle_char)
add_obstacles_horizontally(square_obstacle_grid_2, 2, 7, 3, obstacle_char)
add_obstacles_vertically(square_obstacle_grid_2, 2, 2, 3, obstacle_char)
add_obstacles_vertically(square_obstacle_grid_2, 2, 4, 3, obstacle_char)
add_obstacles_vertically(square_obstacle_grid_2, 2, 7, 3, obstacle_char)
add_obstacles_vertically(square_obstacle_grid_2, 2, 9, 3, obstacle_char)

add_obstacles_horizontally(square_obstacle_grid_2, 7, 2, 3, obstacle_char)
add_obstacles_horizontally(square_obstacle_grid_2, 7, 7, 3, obstacle_char)
add_obstacles_vertically(square_obstacle_grid_2, 7, 2, 3, obstacle_char)
add_obstacles_vertically(square_obstacle_grid_2, 7, 4, 3, obstacle_char)
add_obstacles_vertically(square_obstacle_grid_2, 7, 7, 3, obstacle_char)
add_obstacles_vertically(square_obstacle_grid_2, 7, 9, 3, obstacle_char)

#preview_grid(square_obstacle_grid_2, "square_obstacle_grid_2")

square_obstacle_grid_3: List[List[str]] = [[' ' for _ in range(10)] for _ in range(10)]

add_obstacles_horizontally(square_obstacle_grid_3, 2, 1, 5, obstacle_char)
add_obstacles_vertically(square_obstacle_grid_3, 2, 5, 3, obstacle_char)
add_obstacles_horizontally(square_obstacle_grid_3, 4, 4, 2, obstacle_char)
add_obstacles_horizontally(square_obstacle_grid_3, 6, 7, 4, obstacle_char)
add_obstacles_vertically(square_obstacle_grid_3, 6, 8, 3, obstacle_char)
add_obstacles_horizontally(square_obstacle_grid_3, 8, 1, 4, obstacle_char)
add_obstacles_vertically(square_obstacle_grid_3, 6, 3, 2, obstacle_char)
add_obstacles_vertically(square_obstacle_grid_3, 8, 4, 2, obstacle_char)
add_obstacles_vertically(square_obstacle_grid_3, 1, 8, 3, obstacle_char)

#preview_grid(square_obstacle_grid_3, "square_obstacle_grid_3")

square_obstacle_grid_4: List[List[str]] = [[' ' for _ in range(10)] for _ in range(10)]

add_obstacles_horizontally(square_obstacle_grid_4, 1, 1, 5, obstacle_char)
add_obstacles_vertically(square_obstacle_grid_4, 1, 5, 4, obstacle_char)
add_obstacles_horizontally(square_obstacle_grid_4, 3, 8, 3, obstacle_char)
add_obstacles_vertically(square_obstacle_grid_4, 3, 8, 6, obstacle_char)
add_obstacles_horizontally(square_obstacle_grid_4, 6, 4, 4, obstacle_char)
add_obstacles_horizontally(square_obstacle_grid_4, 9, 1, 5, obstacle_char)

#preview_grid(square_obstacle_grid_4, "square_obstacle_grid_4")

square_obstacle_grid_5: List[List[str]] = [[' ' for _ in range(10)] for _ in range(10)]

add_obstacles_horizontally(square_obstacle_grid_5, 2, 3, 6, obstacle_char)
add_obstacles_vertically(square_obstacle_grid_5, 2, 8, 4, obstacle_char)
add_obstacles_vertically(square_obstacle_grid_5, 2, 3, 7, obstacle_char)
add_obstacles_horizontally(square_obstacle_grid_5, 8, 3, 3, obstacle_char)
add_obstacles_horizontally(square_obstacle_grid_5, 5, 6, 2, obstacle_char)
add_obstacles_horizontally(square_obstacle_grid_5, 7, 8, 3, obstacle_char)
add_obstacles_vertically(square_obstacle_grid_5, 7, 8, 3, obstacle_char)

#preview_grid(square_obstacle_grid_5, "square_obstacle_grid_5")

square_obstacle_grid_6: List[List[str]] = [[' ' for _ in range(10)] for _ in range(10)]

add_obstacles_vertically(square_obstacle_grid_6, 1, 3, 5, obstacle_char)
add_obstacles_horizontally(square_obstacle_grid_6, 5, 3, 4, obstacle_char)
add_obstacles_horizontally(square_obstacle_grid_6, 8, 1, 6, obstacle_char)
add_obstacles_vertically(square_obstacle_grid_6, 1, 7, 2, obstacle_char)
add_obstacles_horizontally(square_obstacle_grid_6, 8, 9, 2, obstacle_char)

#preview_grid(square_obstacle_grid_6, "square_obstacle_grid_6")

square_obstacle_grid_7: List[List[str]] = [[' ' for _ in range(10)] for _ in range(10)]

add_obstacles_vertically(square_obstacle_grid_7, 1, 3, 4, obstacle_char)
add_obstacles_horizontally(square_obstacle_grid_7, 3, 3, 5, obstacle_char)
add_obstacles_horizontally(square_obstacle_grid_7, 6, 1, 5, obstacle_char)
add_obstacles_horizontally(square_obstacle_grid_7, 6, 8, 3, obstacle_char)
add_obstacles_horizontally(square_obstacle_grid_7, 8, 3, 3, obstacle_char)
add_obstacles_vertically(square_obstacle_grid_7, 5, 5, 4, obstacle_char)
add_obstacles_vertically(square_obstacle_grid_7, 6, 9, 4, obstacle_char)
add_obstacles_vertically(square_obstacle_grid_7, 2, 7, 3, obstacle_char)

#preview_grid(square_obstacle_grid_7, "square_obstacle_grid_7")

square_obstacle_grid_8: List[List[str]] = [[' ' for _ in range(10)] for _ in range(10)]

add_obstacles_vertically(square_obstacle_grid_8, 1, 3, 4, obstacle_char)
add_obstacles_vertically(square_obstacle_grid_8, 8, 2, 3, obstacle_char)
add_obstacles_vertically(square_obstacle_grid_8, 6, 8, 4, obstacle_char)
add_obstacles_vertically(square_obstacle_grid_8, 1, 8, 3, obstacle_char)
add_obstacles_horizontally(square_obstacle_grid_8, 4, 2, 5, obstacle_char)
add_obstacles_horizontally(square_obstacle_grid_8, 8, 2, 7, obstacle_char)
add_obstacles_horizontally(square_obstacle_grid_8, 6, 2, 6, obstacle_char)
add_obstacles_horizontally(square_obstacle_grid_8, 3, 8, 2, obstacle_char)

#preview_grid(square_obstacle_grid_8, "square_obstacle_grid_8")

square_obstacle_grid_9: List[List[str]] = [[' ' for _ in range(10)] for _ in range(10)]

add_obstacles_horizontally(square_obstacle_grid_9, 1, 2, 5, obstacle_char)
add_obstacles_horizontally(square_obstacle_grid_9, 4, 2, 5, obstacle_char)
add_obstacles_horizontally(square_obstacle_grid_9, 6, 2, 6, obstacle_char)
add_obstacles_horizontally(square_obstacle_grid_9, 8, 3, 4, obstacle_char)
add_obstacles_horizontally(square_obstacle_grid_9, 10, 1, 5, obstacle_char)
add_obstacles_vertically(square_obstacle_grid_9, 2, 2, 3, obstacle_char)
add_obstacles_vertically(square_obstacle_grid_9, 1, 9, 6, obstacle_char)
add_obstacles_vertically(square_obstacle_grid_9, 6, 7, 3, obstacle_char)
add_obstacles_vertically(square_obstacle_grid_9, 9, 1, 2, obstacle_char)
add_obstacles_vertically(square_obstacle_grid_9, 9, 9, 3, obstacle_char)

#preview_grid(square_obstacle_grid_9, "square_obstacle_grid_9")

square_obstacle_grid_10: List[List[str]] = [[' ' for _ in range(10)] for _ in range(10)]

add_obstacles_horizontally(square_obstacle_grid_10, 2, 4, 4, obstacle_char)
add_obstacles_horizontally(square_obstacle_grid_10, 5, 4, 4, obstacle_char)
add_obstacles_horizontally(square_obstacle_grid_10, 7, 2, 8, obstacle_char)
add_obstacles_horizontally(square_obstacle_grid_10, 9, 2, 5, obstacle_char)
add_obstacles_horizontally(square_obstacle_grid_10, 4, 1, 3, obstacle_char)
add_obstacles_vertically(square_obstacle_grid_10, 2, 4, 4, obstacle_char)
add_obstacles_vertically(square_obstacle_grid_10, 3, 9, 8, obstacle_char)
add_obstacles_vertically(square_obstacle_grid_10, 7, 4, 3, obstacle_char)
add_obstacles_vertically(square_obstacle_grid_10, 1, 1, 4, obstacle_char)

#preview_grid(square_obstacle_grid_10, "square_obstacle_grid_10")

square_obstacle_grid_11: List[List[str]] = [[' ' for _ in range(10)] for _ in range(10)]

add_obstacles_vertically(square_obstacle_grid_11, 1, 4, 4, obstacle_char)
add_obstacles_vertically(square_obstacle_grid_11, 5, 6, 4, obstacle_char)
add_obstacles_vertically(square_obstacle_grid_11, 6, 9, 4, obstacle_char)
add_obstacles_vertically(square_obstacle_grid_11, 1, 7, 2, obstacle_char)
add_obstacles_horizontally(square_obstacle_grid_11, 4, 3, 7, obstacle_char)
add_obstacles_horizontally(square_obstacle_grid_11, 7, 1, 3, obstacle_char)
add_obstacles_horizontally(square_obstacle_grid_11, 2, 1, 2, obstacle_char)
add_obstacle(square_obstacle_grid_11, 9, 8, obstacle_char)

#preview_grid(square_obstacle_grid_11, "square_obstacle_grid_11")

square_obstacle_grid_12: List[List[str]] = [[' ' for _ in range(10)] for _ in range(10)]

add_obstacles_horizontally(square_obstacle_grid_12, 2, 2, 5, obstacle_char)
add_obstacles_horizontally(square_obstacle_grid_12, 4, 3, 6, obstacle_char)
add_obstacles_horizontally(square_obstacle_grid_12, 7, 2, 6, obstacle_char)
add_obstacles_horizontally(square_obstacle_grid_12, 9, 3, 6, obstacle_char)
add_obstacles_horizontally(square_obstacle_grid_12, 8, 5, 2, obstacle_char)
add_obstacles_horizontally(square_obstacle_grid_12, 5, 6, 4, obstacle_char)
add_obstacle(square_obstacle_grid_12, 3, 7, obstacle_char)


#preview_grid(square_obstacle_grid_12, "square_obstacle_grid_12")

square_obstacle_grid_13: List[List[str]] = [[' ' for _ in range(10)] for _ in range(10)]

add_obstacles_horizontally(square_obstacle_grid_13, 2, 2, 4, obstacle_char)
add_obstacles_horizontally(square_obstacle_grid_13, 3, 4, 4, obstacle_char)
add_obstacles_horizontally(square_obstacle_grid_13, 4, 5, 4, obstacle_char)
add_obstacles_horizontally(square_obstacle_grid_13, 8, 2, 4, obstacle_char)
add_obstacles_horizontally(square_obstacle_grid_13, 7, 5, 4, obstacle_char)
add_obstacle(square_obstacle_grid_13, 6, 9, obstacle_char)
add_obstacle(square_obstacle_grid_13, 9, 8, obstacle_char)
add_obstacle(square_obstacle_grid_13, 10, 7, obstacle_char)

#preview_grid(square_obstacle_grid_13, "square_obstacle_grid_13")

square_obstacle_grid_14: List[List[str]] = [[' ' for _ in range(10)] for _ in range(10)]

add_obstacles_vertically(square_obstacle_grid_14, 6, 4, 4, obstacle_char)
add_obstacles_horizontally(square_obstacle_grid_14, 2, 2, 4, obstacle_char)
add_obstacles_horizontally(square_obstacle_grid_14, 3, 5, 4, obstacle_char)
add_obstacles_horizontally(square_obstacle_grid_14, 5, 3, 4, obstacle_char)
add_obstacles_horizontally(square_obstacle_grid_14, 8, 7, 3, obstacle_char)
add_obstacles_horizontally(square_obstacle_grid_14, 8, 1, 3, obstacle_char)
add_obstacle(square_obstacle_grid_14, 7, 10, obstacle_char)
add_obstacle(square_obstacle_grid_14, 4, 9, obstacle_char)

#preview_grid(square_obstacle_grid_14, "square_obstacle_grid_14")

square_obstacle_grid_15: List[List[str]] = [[' ' for _ in range(10)] for _ in range(10)]

add_obstacles_vertically(square_obstacle_grid_15, 3, 9, 4, obstacle_char)
add_obstacles_vertically(square_obstacle_grid_15, 5, 2, 4, obstacle_char)
add_obstacles_horizontally(square_obstacle_grid_15, 2, 5, 5, obstacle_char)
add_obstacles_horizontally(square_obstacle_grid_15, 9, 2, 5, obstacle_char)
add_obstacles_horizontally(square_obstacle_grid_15, 5, 5, 2, obstacle_char)
add_obstacles_horizontally(square_obstacle_grid_15, 6, 5, 2, obstacle_char)
add_obstacles_horizontally(square_obstacle_grid_15, 2, 2, 2, obstacle_char)
add_obstacles_horizontally(square_obstacle_grid_15, 9, 8, 2, obstacle_char)
add_obstacle(square_obstacle_grid_15, 3, 2, obstacle_char)
add_obstacle(square_obstacle_grid_15, 8, 9, obstacle_char)

#preview_grid(square_obstacle_grid_15, "square_obstacle_grid_15")
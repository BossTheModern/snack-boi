'''
    levels_set.py

    contains levels set that is used to store all levels in the game
'''

from assets.levels.levels import Levels
from assets.levels.level import Level
from assets.teleport_pod.teleport_pods import TeleportPods

from boards.grid_collection import square_obstacle_grid, square_obstacle_grid_2
from boards.grid_collection import square_obstacle_grid_3, square_obstacle_grid_4
from boards.grid_collection import square_obstacle_grid_5, square_obstacle_grid_6
from boards.grid_collection import square_obstacle_grid_7, square_obstacle_grid_8
from boards.grid_collection import square_obstacle_grid_9, square_obstacle_grid_10
from boards.grid_collection import square_obstacle_grid_11, square_obstacle_grid_12
from boards.grid_collection import square_obstacle_grid_13, square_obstacle_grid_14
from boards.grid_collection import square_obstacle_grid_15, square_obstacle_grid_16
from boards.grid_collection import square_obstacle_grid_17, square_obstacle_grid_18
from boards.grid_collection import square_obstacle_grid_19, square_obstacle_grid_20
from boards.grid_collection import square_obstacle_grid_21, square_obstacle_grid_22
from boards.grid_collection import square_obstacle_grid_23, square_obstacle_grid_24
from boards.grid_collection import square_obstacle_grid_25


levels_set: Levels = Levels(
    [Level(square_obstacle_grid), 
     Level(square_obstacle_grid_2),
     Level(square_obstacle_grid_3),
     Level(square_obstacle_grid_4),
     Level(square_obstacle_grid_5),
     Level(square_obstacle_grid_6),
     Level(square_obstacle_grid_7),
     Level(square_obstacle_grid_8),
     Level(square_obstacle_grid_9),
     Level(square_obstacle_grid_10),
     Level(square_obstacle_grid_11),
     Level(square_obstacle_grid_12),
     Level(square_obstacle_grid_13),
     Level(square_obstacle_grid_14),
     Level(square_obstacle_grid_15),
     Level(square_obstacle_grid_16),
     Level(square_obstacle_grid_17),
     Level(square_obstacle_grid_18),
     Level(square_obstacle_grid_19),
     Level(square_obstacle_grid_20),
     Level(square_obstacle_grid_21, teleport_pods=TeleportPods()),
     Level(square_obstacle_grid_22, teleport_pods=TeleportPods()),
     Level(square_obstacle_grid_23, teleport_pods=TeleportPods()),
     Level(square_obstacle_grid_24, teleport_pods=TeleportPods()),
     Level(square_obstacle_grid_25, teleport_pods=TeleportPods()),]
)
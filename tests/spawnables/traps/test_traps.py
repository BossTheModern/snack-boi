'''
    test_traps.py

    Test class for trap game spawnable to test its logic
'''

import unittest
import os
import sys
import copy
from typing import List

current_dir: str = os.path.dirname(os.path.abspath(__file__))
parent_dir: str = os.path.dirname(current_dir)
tests_dir: str = os.path.dirname(parent_dir)
root_dir: str = os.path.dirname(tests_dir)

sys.path.insert(0, root_dir)

from boards.grid_collection import square_obstacle_grid
from assets.traps.traps import Trap
from assets.traps.trap_types import HungerTrap
from assets.traps.trap_types import ParallelDimensionTrap
from assets.snacks.snack import Snack
from assets.player import Player
from boards.board_creator import preview_grid
from utils.consts import HUNGER_TRAPS_LIMIT
from utils.consts import PARALLEL_TRAPS_LIMIT

class TestTraps(unittest.TestCase):
    def test_traps_spawn(self) -> None:
        '''
            Test if spawning traps, both hunger and parallell dimension, works
            correctly on a board with just obstacles
        '''

        snack: Snack = Snack()
        player: Player = Player()
        board: List[List[str]] = copy.deepcopy(square_obstacle_grid)
        traps: List[Trap] = []
        hunger_traps: List[Trap] = []
        parallel_dimension_traps: List[Trap] = []
        occupied_positions: List[List[int]] = []

        for _ in range(HUNGER_TRAPS_LIMIT):
            hunger_traps.append(HungerTrap(snack))
        
        for _ in range(PARALLEL_TRAPS_LIMIT):
            parallel_dimension_traps.append(ParallelDimensionTrap(player))

        traps = hunger_traps + parallel_dimension_traps

        for trap in traps:
            trap.spawn_trap(board, occupied_positions)
            occupied_positions.append(trap._position)
            trap.reveal_trap(board)


        preview_grid(board, 'board with traps spawned')

        self.assertEqual(len(occupied_positions), HUNGER_TRAPS_LIMIT + PARALLEL_TRAPS_LIMIT)
        self.assertEqual(len(hunger_traps), HUNGER_TRAPS_LIMIT)
        self.assertEqual(len(parallel_dimension_traps), PARALLEL_TRAPS_LIMIT)


if __name__ == "__main__":
    unittest.main()

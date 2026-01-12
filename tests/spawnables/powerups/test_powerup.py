'''
    test_powerup.py

    Tets class to test powerups logic
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

from assets.powerups.recon_snack import ReconSnack
from boards.grid_collection import square_obstacle_grid
from assets.traps.traps import Trap
from assets.traps.trap_types import HungerTrap
from assets.traps.trap_types import ParallelDimensionTrap
from assets.player import Player
from assets.snacks.snack import Snack
from assets.snacks.snack_types import NormalSnack
from utils.consts import HUNGER_TRAPS_LIMIT
from utils.consts import PARALLEL_TRAPS_LIMIT
from boards.board_creator import preview_grid
from boards.board_creator import OBSTACLE_CHAR


class TestPowerup(unittest.TestCase):
    def test_powerup_spawn(self) -> None:
        '''
            Test if spawning powerup works correctly
        '''
        
        # Initial setup
        board: List[List[str]] = copy.deepcopy(square_obstacle_grid)
        player: Player = Player()
        snack: Snack = NormalSnack()
        traps: List[Trap] = []
        occupied_positions: List[List[int]] = []
        recon_snack: ReconSnack = ReconSnack()

        # spawn setup
        player.spawn_player(board, OBSTACLE_CHAR)
        snack.spawn_snack(board, occupied_positions)

        for _ in range(HUNGER_TRAPS_LIMIT):
            traps.append(HungerTrap(snack))
        
        for _ in range(PARALLEL_TRAPS_LIMIT):
            traps.append(ParallelDimensionTrap(Player))
        
        for trap in traps:
            trap.spawn_trap(board, occupied_positions)
            trap.reveal_trap(board)
            occupied_positions.append(trap._position)
        
        preview_grid(board, 'board before powerup spawned')
        recon_snack.spawn(board, occupied_positions)
        preview_grid(board, 'board after powerup spawned')

        self.assertIn(recon_snack._entity_char, board[recon_snack._position[0]])
        self.assertNotEqual(board[recon_snack._position[0]][recon_snack._position[1]], HungerTrap(snack)._trap_entity)
        self.assertNotEqual(board[recon_snack._position[0]][recon_snack._position[1]], ParallelDimensionTrap(player)._trap_entity)
        self.assertNotEqual(board[recon_snack._position[0]][recon_snack._position[1]], OBSTACLE_CHAR)
        self.assertNotEqual(board[recon_snack._position[0]][recon_snack._position[1]], player._entity)
        self.assertNotEqual(board[recon_snack._position[0]][recon_snack._position[1]], snack._entity)
        self.assertEqual(board[recon_snack._position[0]][recon_snack._position[1]], recon_snack._entity_char)


if __name__ == "__main__":
    unittest.main()
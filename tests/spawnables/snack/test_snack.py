'''
    test_snack.py

    Test class for snack game spawnable to test its logic
    NOTE: The definitions of the tests for eating snacks may be revised
'''
import unittest
import os
import sys
import copy
from typing import List
import keyboard

current_dir: str = os.path.dirname(os.path.abspath(__file__))
parent_dir: str = os.path.dirname(current_dir)
tests_dir: str = os.path.dirname(parent_dir)
root_dir: str = os.path.dirname(tests_dir)

sys.path.insert(0, root_dir)

from boards.grid_collection import square_obstacle_grid
from assets.snacks.snack import Snack
from assets.snacks.snack_types import NormalSnack
from assets.snacks.snack_types import FakeSnack
from assets.snacks.snack_types import SuperSnack
from assets.traps.trap_types import HungerTrap
from assets.enums.enums import SnackTypes
from boards.board import Board
from assets.position.position2d import Position2D
from assets.player import Player
from utils.consts import HUNGER_TRAPS_LIMIT
from boards.board_creator import OBSTACLE_CHAR

class TestSnack(unittest.TestCase):
    def test_spawn_snack(self) -> None:
        '''
            Test if spawning snacks normally on a board with just 
            obstacles works
        '''
        board: Board = copy.deepcopy(square_obstacle_grid)

        snack: Snack = NormalSnack()
        snack.spawn_snack(board, [])
        board.display()
        print('board with normal snack spawned')

        self.assertEqual(snack._entity, board.at(snack._position.x, snack._position.y))
        self.assertNotEqual(board.at(snack._position.x, snack._position.y), 'X')

    def test_spawn_snack_on_trapped_board(self) -> None:
        '''
            Tests if spawning snack on a board with traps is handled correctly 
        '''
        snack: Snack = NormalSnack()
        board: Board = copy.deepcopy(square_obstacle_grid)
        occupied_positions: List[Position2D] = []

        for _ in range(HUNGER_TRAPS_LIMIT):
            trap: HungerTrap = HungerTrap(snack)
            trap.spawn_trap(board, occupied_positions)
            trap.reveal_trap(board)
            occupied_positions.append(trap._position)
        
        board.display()
        print('board with traps spawned')
        snack.spawn_snack(board, occupied_positions)
        board.display()
        print('board with snack spawned')

        self.assertEqual(snack._entity, board.at(snack._position.x, snack._position.y))
        self.assertNotEqual(board.at(snack._position.x, snack._position.y), 'X')
        self.assertNotEqual(board.at(snack._position.x, snack._position.y), 'H')


    def test_eat_snack(self) -> None:
        '''
            Test if eating normal snacks works as intended
        '''

        # Initial setup        
        snack: Snack = NormalSnack()
        player: Player = Player()
        board: Board = copy.deepcopy(square_obstacle_grid)
        old_count: int = 0

        # Setup and move player to snack position
        player._position = Position2D(4, 5)
        board.set(player._position.x, player._position.y, player._entity)
        snack._position = Position2D(5, 5)
        board.set(snack._position.x, snack._position.y, snack._entity)
        board.display()
        print('board with player and normal snack spawned')
        
        player.move_player(keyboard.KeyboardEvent('down', 1, 'd'), board, OBSTACLE_CHAR, player._position)
        if player._position == snack._position and snack._type == SnackTypes.NORMAL.value:
            snack._count += 1
            snack._position.clear()
        board.display()
        print('board with player after eating normal snack')
        
        self.assertEqual(snack._count - old_count, 1)

    
    def test_eat_fake_snack(self) -> None:
        '''
            Test if eating fake snacks works correctly
        '''

        # Initial setup        
        snack: Snack = FakeSnack()
        player: Player = Player()
        board: Board = copy.deepcopy(square_obstacle_grid)
        old_count: int = snack._count

        # Setup and move player to snack position
        player._position = Position2D(4, 5)
        board.set(player._position.x, player._position.y, player._entity)
        snack._position = Position2D(5, 5)
        board.set(snack._position.x, snack._position.y, snack._entity)
        board.display()
        print('board with player and normal snack spawned')
        
        player.move_player(keyboard.KeyboardEvent('down', 1, 'd'), board, OBSTACLE_CHAR, player._position)
        if player._position == snack._position and snack._type == SnackTypes.FAKE.value:
            snack._position.clear()
        board.display()
        print('board with player after eating fake snack')

        self.assertEqual(snack._count, old_count)

    def test_eat_super_snack(self) -> None:
        '''
            Test if eating fake snacks works correctly
        '''

        # Initial setup        
        snack: Snack = SuperSnack()
        player: Player = Player()
        board: Board = copy.deepcopy(square_obstacle_grid)
        old_count: int = snack._count

        # Setup and move player to snack position
        player._position = Position2D(4, 5)
        board.set(player._position.x, player._position.y, player._entity)
        snack._position = Position2D(5, 5)
        board.set(snack._position.x, snack._position.y, snack._entity)
        board.display()
        print('board with player and super snack spawned')
        
        player.move_player(keyboard.KeyboardEvent('down', 1, 'd'), board, OBSTACLE_CHAR, player._position)
        if player._position == snack._position and snack._type == SnackTypes.SUPER.value:
            snack._count += 2
            snack._position.clear()
        board.display()
        print('board with player after eating super snack')

        self.assertEqual(snack._count - old_count, 2)

        

if __name__ == "__main__":
    unittest.main()
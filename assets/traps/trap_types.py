'''
    trap_types.py

    Handles logic for different types of traps. All of them are children of
    Trap class
'''
from traps import Trap
from typing import List
from player import Player
from keyboard import KeyboardEvent
from hidden_trigger import HiddenTrigger
from dimension_exit import DimensionExit
import keyboard
import os
import sys
import random
import copy

current_dir: str = os.path.dirname(os.path.abspath(__file__))
parent_dir: str = os.path.dirname(current_dir)
parent_parent_dir: str = os.path.dirname(parent_dir)
boards_dir: str = os.path.join(parent_parent_dir, 'boards')
printer_dir: str = os.path.join(parent_dir, 'printer')
snacks_dir: str = os.path.join(parent_dir, 'snacks')

sys.path.insert(0, boards_dir)
sys.path.insert(0, printer_dir)
sys.path.insert(0, snacks_dir)

from grid_collection import empty_grid
from board_creator import draw_grid, OBSTACLE_CHAR
from fancy_printer import FancyPrinter
from snack import Snack

class HungerTrap(Trap):
    '''
        Hunger trap that reduces snack count upon stepping on it
    '''
    def __init__(self, snack: Snack) -> None:
        self._trap_entity: str = 'H'
        self._type: str = 'hunger'
        self._snack: Snack = snack
        self._position: List[int] = []
    
    def reduce_snack_count(self, board: List[List[str]], occupied_positions: List[List[int]]) -> None:
        '''
            Reduces the snack count by a random amount between 1 and 3.

            Args:
                board: board that the trap will spawn on once it has been eaten
        '''
        reduce_amount: int = random.randint(1, 3)
        
        if self._snack._count - reduce_amount >= 0: 
            self._snack._count -= reduce_amount 
        else:
            self._snack._count = 0

        print(f"Snack count reduced by {reduce_amount}. Current snack count: {self._snack._count}")

        self._position.clear()
        self.spawn_trap(board, occupied_positions)


class ParallelDimensionTrap(Trap):
    '''
        Parallel dimension trap that sends players to an empty parallel
        dimension upon triggering it
    '''
    def __init__(self, player: Player) -> None:
        self._player: Player = player
        self._trap_entity: str = 'Ø'
        self._type: str = 'parallel dimension'
        self._parallel_board: List[List[str]] = copy.deepcopy(empty_grid)
        self._position: List[int] = []
        self._hidden_trigger: HiddenTrigger = HiddenTrigger()
        self._exit: DimensionExit = DimensionExit()
        self._valid_move_keys: List[str] = ['w', 'a', 's', 'd']
        self._fancy_printer: FancyPrinter = FancyPrinter(interval = 0.02, line_interval = 0.5)
    
    def print_parallel_dimension(self) -> None:
        print("-----------[PARALLEL DIMENSION]-----------")
        draw_grid(self._parallel_board)
        print("Move by pressing (w/a/s/d)")
    
    def teleport_player(self, game_mode: str) -> None:
        '''
            Teleports the player to a parallel dimension
            Once the player is teleported, they have to find a hidden trigger.
            When the hidden trigger is found, it will activate the exit 
            allowing the player to escape
        '''
        key_event: KeyboardEvent
        show_board: bool = True
        printed_dialogue: bool = False
        found_trigger: bool = False

        # teleport player specific functions
        def show_initial_dialogue() -> None:
            text: str = "Where am I? This place is empty...\n" \
                        "I need to find something here\n" \
                        "Hahaha, good luck finding that. You might starve before you even get out\n"
            
            self._fancy_printer.print_text_line(text)

        # Initial spawn
        self._player.parallel_spawn_player(self._parallel_board)
        self._hidden_trigger.spawn(self._parallel_board)

        # Parallel dimension loop
        while True:
            if show_board:
                self.print_parallel_dimension()
                show_board = False
            
            if not printed_dialogue and game_mode == 'classic':
                show_initial_dialogue()
                printed_dialogue = True    
            
            if found_trigger:
                print("Ah, there's the exit!")
                found_trigger = False
            
            key_event = keyboard.read_event(suppress=True)

            # Handle player movement in parallel dimension
            if key_event.event_type == keyboard.KEY_DOWN and key_event.name in self._valid_move_keys:
                self._player.move_player(key_event, self._parallel_board, OBSTACLE_CHAR, self._player._parallel_position)
                show_board = True

            # Handle player finding hidden trigger
            if self._player._parallel_position == self._hidden_trigger._position:
                self._exit.spawn(self._parallel_board)
                self._hidden_trigger._position.clear()
                found_trigger = True
            
            # Handle player finding the exit
            if self._player._parallel_position == self._exit._position:
                self._exit._position.clear()
                break
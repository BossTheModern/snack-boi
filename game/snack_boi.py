'''
    snack_boi.py
    
    Game module for where the main game logic lies for both classic and 
    endless gamemode
'''

# TODO: 
# - Find a way to fix display bug when eating hunger trap (player disappears upon eating revealed hunger trap)
# - Refactor toggle text display (mvoe to a separate module)

import keyboard
import random
from typing import List
from keyboard import KeyboardEvent
from utils import consts
from utils import debug
from utils import keyboard_utils
from utils import game_utils
from boards.board_creator import OBSTACLE_CHAR
from assets.levels.levels import Levels
from assets.snacks.snack import Snack
from assets.snacks.snack_types import SuperSnack, FakeSnack, NormalSnack
from assets.save_file import SaveFile
from assets.levels.level import Level
from assets.menu import Menu
from assets.player import Player
from assets.traps.traps import Trap
from assets.traps.trap_types import HungerTrap, ParallelDimensionTrap
from assets.powerups.recon_snack import ReconSnack
from assets.printer.fancy_printer import FancyPrinter
from assets.text_collection import TextCollection


# Game class where the game logic is implemented
class Game:    
    # Validation properties 
    _valid_move_keys: List[str] = ['w', 'a', 's', 'd']
    _main_menu_options: List[str] = ['1', '2', '3', '4']

    # Player and snack related properties
    _player: Player = Player()
    _snack: Snack = Snack()
    _normal_snack: NormalSnack = NormalSnack()
    _super_snack: SuperSnack = SuperSnack()
    _fake_snack: FakeSnack = FakeSnack()
    
    _current_snack: Snack = Snack()

    # Trap related properties
    _hunger_traps: List[Trap] = []
    _parallel_dimension_traps: List[Trap] = []
    _traps: List[Trap] = []

    # Powerup related properties
    _recon_snack: ReconSnack = ReconSnack()
    _recon_duration: int = 3
    
    # Levels related properties
    _new_levels: Levels = Levels()
    _classic_levels: List[Level] = _new_levels._classic_levels_set_1

    # Other properties
    _save_file: SaveFile = SaveFile('assets/save_files/save_file.txt')
    _fancy_print: FancyPrinter = FancyPrinter()
    _text_collection: TextCollection = TextCollection()

    def __init__(self) -> None:
        self.menu: Menu = Menu(self.game_loop)
        self._game_utils: game_utils.GameUtils = game_utils.GameUtils(self._snack)
    
    def eat_snack(self, current_lvl_index: int) -> None:
        '''
            Handles eating snack based on whether the player have reached
            a minimum level for newer snacks or not
        '''
        if current_lvl_index >= consts.NEW_SNACKS_START_LVL-1:
            match self._current_snack._type:
                case 'normal':
                    self._snack._count += 1
                case 'super':
                    self._snack._count += 2
            self._snack._position.clear()            
        
        else:
            print("Snack eaten!")
            self._snack._count += 1
    
    def clear_game_data(self) -> None:
        self._player._position.clear()
        self._player._parallel_position.clear()
        self._snack._position.clear()
        self._snack._count = 0
        self._hunger_traps.clear()
        self._parallel_dimension_traps.clear()
        self._traps.clear()
        self._recon_snack._position.clear()
        self._recon_snack._eaten_counter = 0
        self._recon_snack._counter = 0
        self._game_utils.clear_toggle_text()

    def game_spawn_snack(self, grid: List[List[str]], occupied_positions: List[List[int]], snack_num: int) -> None:
        '''
            Spawns snack based on the snack number generated on the board
        '''
        match snack_num:
            case 1:
                self._normal_snack.spawn_snack(grid, occupied_positions)
                self._current_snack = self._normal_snack
            case 2:
                self._fake_snack.spawn_snack(grid, occupied_positions)
                self._current_snack = self._fake_snack
            case 3:
                self._super_snack.spawn_snack(grid, occupied_positions)
                self._current_snack = self._super_snack
    
    def activate_hunger_trap(self, hunger_trap: HungerTrap, board: List[List[str]], occupied_positions: List[List[int]]) -> None:
            hunger_trap.reduce_snack_count(board, occupied_positions)

    def actiavte_parallel_trap(self, parallel_trap: ParallelDimensionTrap, game_mode: str) -> None:
            parallel_trap.teleport_player(game_mode)
            self._traps.remove(parallel_trap)
        
    
    def game_loop(self, board: List[List[str]], game_mode: str) -> None:
        '''
            Main game loop that runs based on game mode
            Game mode is classic: the game has a set win cap to collect to
            Game mode is endless: no win cap, just snack count. Player need to
                                  press q to quit endless mode
        '''
        current_level_index: int = 0
        random_snack_num: int = 0
        key_event: KeyboardEvent
        show_state: bool = True
        intro_show_state: bool = True
        recon_duration: int = self._recon_snack._duration
        trap: Trap
        occupied_positions: List[List[int]] = []
        levels_unlocked: int = 0
        
        # Eating flags for one time display
        recon_start_reached: bool = False

        for level in self._classic_levels:
            if level._selected:
                break
            current_level_index += 1
        
        # Game setup
        self._player.spawn_player(board, OBSTACLE_CHAR)

        # Add new snack logic available starting from certain levels
        if current_level_index >= consts.NEW_SNACKS_START_LVL-1:
            random_snack_num = random.randint(1, 3)
            self.game_spawn_snack(board, occupied_positions, random_snack_num)
            occupied_positions.append(self._current_snack._position)
        else:
            self._normal_snack.spawn_snack(board, occupied_positions)
            self._current_snack = self._normal_snack
            occupied_positions.append(self._current_snack._position)

        
        # Enable traps and spawn them starting from a set level
        # Enable recon snack starting from the same level
        if current_level_index >= consts.TRAP_START_LVL-1:            
            for _ in range(consts.HUNGER_TRAPS_LIMIT):
                self._hunger_traps.append(HungerTrap(self._snack))
            
            for _ in range(consts.PARALLEL_TRAPS_LIMIT):
                self._parallel_dimension_traps.append(ParallelDimensionTrap(self._player))
                        
            self._traps = self._hunger_traps + self._parallel_dimension_traps

            for trap in self._traps:
                trap.spawn_trap(board, occupied_positions)
                occupied_positions.append(trap._position)
            
            recon_start_reached = True
        
        levels_unlocked = len([lvl for lvl in self._classic_levels if lvl._unlocked == True])

        # Game loop handling both modes
        while True:
            # Intro text before game display
            # if intro_show_state:
            #     match levels_unlocked:
            #         case 1: self._fancy_print.print_text_line(self._text_collection._start_intro)
            #         case consts.NEW_SNACKS_START_LVL: self._fancy_print.print_text_line(self._text_collection._extra_snack_intro)
            #         case consts.TRAP_START_LVL: self._fancy_print.print_text_line(self._text_collection._traps_intro)
            #         case _: print("Nothing to show")

            #     intro_show_state = False
            
            # Handle win condition
            if game_mode == 'classic':
                if self._snack._count >= self._classic_levels[current_level_index]._win_cap:
                    self._game_utils.classic_game_win(current_level_index, self._classic_levels)
                    break
            
            if show_state:
                match game_mode:
                    case 'classic':
                        self._game_utils.classic_display_current_state(board, current_level_index, self._classic_levels)
                    case 'endless':
                        self._game_utils.endless_display_current_state(board, current_level_index, self._classic_levels)
                    case _:
                        print("Nothing to display")

                print("Move by pressing (w/a/s/d) or press q to quit")
                print("Super snack spawned! Eat it for extra points!") if self._current_snack._type == 'super' else None
                print(f"Recon duration: {recon_duration} moves") if self._recon_snack._active else None
                
                # Supplementary toggle text
                self._game_utils.toggleText()
                
                # Object tracker for debugging purposes
                # debug.print_obj_tracker(occupied_positions, self._current_snack, self._traps, self._recon_snack)
                show_state = False            

            key_event = keyboard.read_event(suppress=True)

            if keyboard_utils.check_key_event(key_event, 'q'):
                break
            
            # Handle player movement
            if key_event.event_type == keyboard.KEY_DOWN and key_event.name in self._valid_move_keys:
                self._player.move_player(key_event, board, OBSTACLE_CHAR, self._player._position)

                if self._recon_snack._active:
                    recon_duration -= 1
                show_state = True
                
                # handle recon snack duration
                if recon_duration <= 0:
                    self._recon_snack.undo_effect(board, self._traps)
                    recon_duration = self._recon_snack._duration

            # Handle eating snack
            if self._player._position == self._current_snack._position:
                if recon_start_reached:
                    self._recon_snack._eaten_counter += 1
                
                self.eat_snack(current_level_index)
                occupied_positions.remove(self._current_snack._position)

                match self._current_snack._type:
                    case 'normal': self._game_utils._snack_eaten = True
                    case 'super': self._game_utils._super_snack_eaten = True
                    case 'fake': self._game_utils._fake_snack_eaten = True

                # Spawn new snack and handle new snacks starting from a set level
                if current_level_index >= consts.NEW_SNACKS_START_LVL-1:
                    random_snack_num = random.randint(1, 3)
                    self.game_spawn_snack(board, occupied_positions, random_snack_num)
                    occupied_positions.append(self._current_snack._position)
                else:
                    self._normal_snack.spawn_snack(board, occupied_positions)
                    self._current_snack = self._normal_snack
                    occupied_positions.append(self._current_snack._position)

            # Recon snack count requirement for spawning recon snack
            if self._recon_snack._eaten_counter >= self._recon_snack._required_eaten_snacks and self._recon_snack._counter < self._recon_snack._max_number:
                self._recon_snack.spawn(board, occupied_positions)
                self._game_utils._recon_spawned = True
                occupied_positions.append(self._recon_snack._position)
            
            # Handle eating recon snack
            if self._player._position == self._recon_snack._position:
                self._recon_snack.reveal_position(board, self._traps)
                self._game_utils._traps_revealed = True
                occupied_positions.remove(self._recon_snack._position)
            
            # Handle player eating any trap
            trap = next((t for t in self._traps if t._position == self._player._position), None)
            if trap:
                # Check type and activate accordingly
                match trap._type:
                    case 'hunger': 
                        occupied_positions.remove(trap._position)
                        self.activate_hunger_trap(trap, board, occupied_positions)
                        occupied_positions.append(trap._position)
                        self._game_utils._hunger_trap_eaten = True
                    case 'parallel dimension': 
                        self.actiavte_parallel_trap(trap, game_mode)
                        occupied_positions.remove(trap._position)
                        self._game_utils._parallel_trap_eaten = True
                    case _: print("No type found")                
        
        self.clear_game_data()
        print("Quitting game, back to main menu")

    def game_menu(self) -> None:
        '''
            Game's main menu with saving prompt upon closing the game
        '''
        key_event: KeyboardEvent
        show_menu: bool = True

        self.menu.print_welcome_screen()
        self._save_file.load(self._classic_levels)

        # Main menu loop
        while True:
            if show_menu:
                self.menu.print_game_menu(consts.VERSION, self._main_menu_options)
                show_menu = False

            key_event = keyboard.read_event(suppress=True)

            if keyboard_utils.check_key_event(key_event, self._main_menu_options[0]):
                self.menu.mode_selection_menu(self._classic_levels)
                show_menu = True
            elif keyboard_utils.check_key_event(key_event, self._main_menu_options[1]):
                self.menu.game_options(self._classic_levels, self._save_file)
                show_menu = True
            elif keyboard_utils.check_key_event(key_event, self._main_menu_options[2]):
                self.menu.version_log()
                show_menu = True
            elif keyboard_utils.check_key_event(key_event, self._main_menu_options[3]):
                break
        
        self._save_file.save_prompt(key_event, self._classic_levels) if not self._save_file._already_saved else None
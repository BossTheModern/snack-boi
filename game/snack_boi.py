'''
    snack_boi.py
    
    Game module for where the main game logic lies for both classic and 
    endless gamemode
'''
import sys
import os
import keyboard
import random
from typing import List
from keyboard import KeyboardEvent

current_dir: str = os.path.dirname(os.path.abspath(__file__))
parent_dir: str = os.path.dirname(current_dir)
boards_path: str = os.path.join(parent_dir, 'boards')
assets_path: str = os.path.join(parent_dir, 'assets')
save_files_path: str = os.path.join(assets_path, 'save_files')
powerups_path: str = os.path.join(assets_path, 'powerups')
printer_path: str = os.path.join(assets_path, 'printer')
traps_path: str = os.path.join(assets_path, 'traps')
levels_path: str = os.path.join(assets_path, 'levels')
snacks_path: str = os.path.join(assets_path, 'snacks')

sys.path.insert(0, boards_path)
sys.path.insert(0, assets_path)
sys.path.insert(0, powerups_path)
sys.path.insert(0, printer_path)
sys.path.insert(0, traps_path)
sys.path.insert(0, snacks_path)
sys.path.insert(0, levels_path)

from utils import consts
from utils import debug
from board_creator import draw_grid, OBSTACLE_CHAR
from levels import Levels
from snack import Snack
from snack_types import SuperSnack, FakeSnack, NormalSnack
from save_file import SaveFile
from level import Level
from menu import Menu
from player import Player
from traps import Trap
from trap_types import HungerTrap, ParallelDimensionTrap
from recon_snack import ReconSnack
from fancy_printer import FancyPrinter
from text_collection import TextCollection


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
    _current_snack: Snack
    _previous_snack: Snack

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
    _save_file: SaveFile = SaveFile(os.path.join(save_files_path, 'save_file.txt'))
    _fancy_print: FancyPrinter = FancyPrinter()
    _text_collection: TextCollection = TextCollection()

    def __init__(self) -> None:
        self.menu: Menu = Menu(self.game_loop)
    
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

    def check_key_event(self, key_event: KeyboardEvent, target_key: str):
        return key_event.event_type == keyboard.KEY_DOWN and key_event.name == target_key
    
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
        recon_duration: int = self._recon_duration
        trap: Trap
        occupied_positions: List[List[int]] = []
        levels_unlocked: int = 0
        
        # Eating flags for one time display
        parallel_trap_eaten: bool = False
        hunger_trap_eaten: bool = False
        snack_eaten: bool = False
        super_snack_eaten: bool = False
        fake_snack_eaten: bool = False
        recon_start_reached: bool = False

        for level in self._classic_levels:
            if level._selected:
                break
            current_level_index += 1
        
        # Game loop specific functions
        def classic_display_current_state(grid: List[List[str]], 
                                      current_lvl_index: int) -> None:
            print(f"--------[CLASSIC MODE - {self._classic_levels[current_lvl_index]._level_name}]--------")
            draw_grid(grid)
            print(f"{self._snack._count}/{self._classic_levels[current_lvl_index]._win_cap} snacks eaten")
        
        def endless_display_current_state(grid: List[List[str]], 
                                      current_lvl_index: int) -> None:
            print(f"--------[ENDLESS MODE - {self._classic_levels[current_lvl_index]._level_name}]--------")
            draw_grid(grid)
            print("Snack count:", self._snack._count)
        
        def classic_game_win(current_lvl_index: int) -> None:
            '''
                Handles winning logic for classic game mode
            '''
            next_level_index: int
            print("You win! You have eaten enough snacks!")

            if current_lvl_index + 1 <= len(self._classic_levels)-1:
                next_level_index = current_lvl_index + 1

                if not self._classic_levels[next_level_index]._unlocked:
                    self._classic_levels[next_level_index]._unlocked = True
                    print("Next level unlocked")

            if not self._classic_levels[current_lvl_index]._cleared:
                print(f"Endless mode for {self._classic_levels[current_lvl_index]._level_name} unlocked!")
                self._classic_levels[current_lvl_index]._cleared = True
        
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
            self._previous_snack = self._current_snack
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
            if intro_show_state:
                match levels_unlocked:
                    case 1: self._fancy_print.print_text_line(self._text_collection._start_intro)
                    case consts.NEW_SNACKS_START_LVL: self._fancy_print.print_text_line(self._text_collection._extra_snack_intro)
                    case consts.TRAP_START_LVL: self._fancy_print.print_text_line(self._text_collection._traps_intro)
                    case _: print("Nothing to show")

                intro_show_state = False
            
            # Handle win condition
            if game_mode == 'classic':
                if self._snack._count >= self._classic_levels[current_level_index]._win_cap:
                    classic_game_win(current_level_index)
                    break
            
            if show_state:
                match game_mode:
                    case 'classic':
                        classic_display_current_state(board, current_level_index)
                    case 'endless':
                        endless_display_current_state(board, current_level_index)
                    case _:
                        print("Nothing to display")

                print("Move by pressing (w/a/s/d) or press q to quit")
                print("Super snack spawned! Eat it for extra points!") if self._current_snack._type == 'super' else None
                print(f"Recon duration: {recon_duration} moves") if self._recon_snack._active else None
                
                # Supplementary toggle text
                if self._recon_snack._spawned:
                    print("Oh, I see a powerup over there. Let's get it!") 
                    self._recon_snack._spawned = False

                if self._recon_snack._traps_revealed:
                    print("I can see the traps plain as day!")
                    self._recon_snack._traps_revealed = False
                
                if hunger_trap_eaten:
                    print("Oh no! I feel so hungry...")
                    hunger_trap_eaten = False
                
                if parallel_trap_eaten:
                    print("Getting out of here, see ya later!")
                    parallel_trap_eaten = False
                
                if snack_eaten:
                    print("Nom nom")
                    snack_eaten = False
                
                if fake_snack_eaten:
                    print("What!? That snack was fake!")
                    fake_snack_eaten = False
                
                if super_snack_eaten:
                    print("Yum! That one was delicious!")
                    super_snack_eaten = False
                
                # Object tracker for debugging purposes
                # debug.print_obj_tracker(occupied_positions, self._current_snack, self._traps, self._recon_snack)
                show_state = False            

            key_event = keyboard.read_event(suppress=True)

            if self.check_key_event(key_event, 'q'):
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
                    self._recon_snack._eaten_counter = 0
                    self._recon_snack._counter -= 1
                    self._recon_snack._active = False

            # Handle eating snack
            if self._player._position == self._current_snack._position:
                if recon_start_reached:
                    self._recon_snack._eaten_counter += 1
                
                self.eat_snack(current_level_index)
                occupied_positions.remove(self._current_snack._position)

                match self._current_snack._type:
                    case 'normal': snack_eaten = True
                    case 'super': super_snack_eaten = True
                    case 'fake': fake_snack_eaten = True

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
                self._recon_snack._counter += 1
                self._recon_snack._spawned = True
                occupied_positions.append(self._recon_snack._position)
            
            # Handle eating recon snack
            if self._player._position == self._recon_snack._position:
                self._recon_snack.reveal_position(board, self._traps)
                self._recon_snack._position.clear()
                self._recon_snack._traps_revealed = True
                self._recon_snack._active = True
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
                        hunger_trap_eaten = True
                    case 'parallel dimension': 
                        self.actiavte_parallel_trap(trap, game_mode)
                        occupied_positions.remove(trap._position)
                        parallel_trap_eaten = True
                    case _: print("No type found")                
        
        self.clear_game_data()
        print("Quitting game, back to main menu")

    def game_menu(self) -> None:
        '''
            Game's main menu with saving prompt upon closing the game
        '''
        key_event: KeyboardEvent
        show_menu: bool = True

        def save_prompt() -> None:
            print("Do you want to save your progress? (y/n)")
            while True:
                key_event = keyboard.read_event(suppress=True)
                if key_event.event_type == keyboard.KEY_DOWN and key_event.name in ['y', 'n']:
                    break
            if key_event.name == 'y':
                print("Saving progress...")
                self._save_file.save(self._classic_levels)
            elif key_event.name == 'n':
                print("Progress kept as it is")

        self.menu.print_welcome_screen()

        self._save_file.load(self._classic_levels)

        # Main menu loop
        while True:
            if show_menu:
                self.menu.print_game_menu(consts.VERSION, self._main_menu_options)
                show_menu = False

            key_event = keyboard.read_event(suppress=True)

            if self.check_key_event(key_event, self._main_menu_options[0]):
                self.menu.mode_selection_menu(self._classic_levels)
                show_menu = True
            elif self.check_key_event(key_event, self._main_menu_options[1]):
                self.menu.game_options(self._classic_levels, self._save_file)
                show_menu = True
            elif self.check_key_event(key_event, self._main_menu_options[2]):
                self.menu.version_log()
                show_menu = True
            elif self.check_key_event(key_event, self._main_menu_options[3]):
                break
        
        save_prompt() if not self._save_file._already_saved else None
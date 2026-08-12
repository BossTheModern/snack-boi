'''
    snack_boi.py
    
    Game module for where the main game logic lies for both classic and 
    endless gamemode
'''

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
from assets.menu_front import MenuFront
from account.account import Account
from assets.shop.shop_item import ShopItem
from boards.board import Board
from utils.consts import EMPTY_SHOP_ITEM
import copy


# Game class where the game logic is implemented
class Game:    
    # Validation properties 
    _valid_move_keys: List[str] = ['w', 'a', 's', 'd']
    _main_menu_options: List[str] = ['1', '2', '3', '4', '5', '6']

    # Player and snack related properties
    _player: Player = Player()
    _snack: Snack = Snack()
    _normal_snack: NormalSnack = NormalSnack()
    _super_snack: SuperSnack = SuperSnack()
    _fake_snack: FakeSnack = FakeSnack()
    _current_snack: Snack = Snack()
    
    # Powerup related properties
    _recon_snack: ReconSnack = ReconSnack()
    
    # Levels related properties
    _new_levels: Levels = Levels()
    _classic_levels: List[Level] = _new_levels._classic_levels_set_1

    # Other properties
    _menu_front: MenuFront = MenuFront()
    _account: Account = Account()

    # Active shop powerup
    _active_shop_powerup: ShopItem = EMPTY_SHOP_ITEM

    def __init__(self) -> None:
        self._save_file: SaveFile = SaveFile(consts.SAVE_FILE_PATH, self._account)
        self.menu: Menu = Menu(self.game_loop, self._account)
        self._game_utils: game_utils.GameUtils = game_utils.GameUtils(self._snack)
    
    def clear_game_data(self) -> None:
        self._player.clear_data()
        self._snack.clear_data()
        self._recon_snack.clear_data()
        self._game_utils.clear_toggle_text()
        self._active_shop_powerup: ShopItem = EMPTY_SHOP_ITEM

    def clear_owned_items(self, game_mode: str, current_level_index: int) -> None:
        # Determine if usage of active powerup is complete
        if game_mode == "classic" and self._snack._count >= self._classic_levels[current_level_index]._win_cap and (self._active_shop_powerup.reached_usage_per_game() or self._active_shop_powerup._active):
            self._active_shop_powerup.complete_usage()
        elif game_mode == "endless" and self._active_shop_powerup.reached_usage_per_game():
            self._active_shop_powerup.complete_usage()
        

        self._active_shop_powerup.reset()

        # Update with used powerup and erase ones with zero quantity
        self._account._owned_shop_items = [self._active_shop_powerup if self._active_shop_powerup._name == powerup._name else powerup for powerup in self._account._owned_shop_items ]
        self._account._owned_shop_items = [powerup for powerup in self._account._owned_shop_items if powerup._stock > 0]

    def game_spawn_snack(self, board: Board, occupied_positions: List[List[int]], snack_num: int) -> None:
        '''
            Spawns snack based on the snack number generated on the board 
        '''
        match snack_num:
            case 1:
                self._normal_snack.spawn_snack(board, occupied_positions)
                self._current_snack = self._normal_snack
            case 2:
                self._fake_snack.spawn_snack(board, occupied_positions)
                self._current_snack = self._fake_snack
            case 3:
                self._super_snack.spawn_snack(board, occupied_positions)
                self._current_snack = self._super_snack

    def activate_parallel_trap(self, parallel_trap: ParallelDimensionTrap, game_mode: str) -> None:
            parallel_trap.teleport_player(game_mode)
        
    
    def game_loop(self, board: Board, game_mode: str) -> None:
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
        hunger_traps: List[Trap] = []
        parallel_dimension_traps: List[Trap] = []
        traps: List[Trap] = []
        
        owned_powerups: List[ShopItem] = self._account._owned_shop_items
        powerup_index: int
        tracked_positions: List[List[int]] = []

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
                hunger_traps.append(HungerTrap(self._snack))
            
            for _ in range(consts.PARALLEL_TRAPS_LIMIT):
                parallel_dimension_traps.append(ParallelDimensionTrap(self._player))
                        
            traps = hunger_traps + parallel_dimension_traps

            for trap in traps:
                trap.spawn_trap(board, occupied_positions)
                occupied_positions.append(trap._position)
            
            recon_start_reached = True
        
        levels_unlocked = len([lvl for lvl in self._classic_levels if lvl._unlocked == True])

        # Prompt user to choose a powerup if they have any
        if owned_powerups:
            powerup_index = self.menu.prompt_powerup_selection(owned_powerups)
            if powerup_index >= 0:
                self._active_shop_powerup = owned_powerups[powerup_index]
        
        # Start precording positions for recall gadget
        if self._active_shop_powerup._name == "Recall":
            self._active_shop_powerup.prerecord_last_positions(self._player._position)
            tracked_positions.append(self._player._position.copy())


        # Game loop handling both modes
        while True:
            # Intro text before game display
            if intro_show_state and game_mode == 'classic':
                self._game_utils.intro_text_display(levels_unlocked, current_level_index)
                intro_show_state = False
            
            # Handle win condition
            if game_mode == 'classic' and self._snack._count >= self._classic_levels[current_level_index]._win_cap:
                self._game_utils.classic_game_win(current_level_index, self._classic_levels, self._account)
                break
            
            

            if show_state:
                self._game_utils.display_current_state(board, current_level_index, 
                                                       self._classic_levels, 
                                                       game_mode, self._current_snack._type, 
                                                       recon_duration, self._recon_snack._active,
                                                       self._active_shop_powerup)
                
                # Object tracker for debugging purposes
                # debug.print_obj_tracker(occupied_positions, self._current_snack, traps, self._recon_snack)
                show_state = False            

            key_event = keyboard.read_event(suppress=True)

            if keyboard_utils.check_key_event(key_event, 'q'):
                break

            # Toggle active powerup
            if keyboard_utils.check_key_event(key_event, 'e') and not self._active_shop_powerup._active and not self._active_shop_powerup.reached_usage_per_game():
                self._active_shop_powerup.activate()
                show_state = True
            
             # Handle player movement
            if key_event.event_type == keyboard.KEY_DOWN and key_event.name in self._valid_move_keys:
                self._player.move_player(key_event, board, OBSTACLE_CHAR, self._player._position)

                if self._recon_snack._active:
                    recon_duration -= 1
                show_state = True
                
                # handle recon snack duration
                if recon_duration <= 0:
                    self._recon_snack.undo_effect(board, traps)
                    recon_duration = self._recon_snack._duration
                
                # Handle registering previous position
                if self._active_shop_powerup._name == "Recall":
                    if len(tracked_positions) == 2:
                        tracked_positions[1] = tracked_positions[0].copy()
                        tracked_positions[0] = self._player._position.copy()
                    else:
                        tracked_positions.append(self._player._position.copy())
                    

                    match len(self._active_shop_powerup._previous_positions):
                        case 1:
                            self._active_shop_powerup.prerecord_last_positions(self._player._position.copy())
                            self._active_shop_powerup._previous_positions.reverse()
                        case _:
                            self._active_shop_powerup.record_last_positions(self._player._position.copy(), tracked_positions.copy())

                    # Handle maintaining unit 
                    if self._player._position != self._active_shop_powerup._position and self._active_shop_powerup._placed:
                        board.set(self._active_shop_powerup._position[0], self._active_shop_powerup._position[1], self._active_shop_powerup._entity)
                    
                    # Ensure recording order is correct
                    if self._player._position == self._active_shop_powerup._previous_positions[0]:
                        self._active_shop_powerup._previous_positions.reverse()

            # Handle area scan
            if self._active_shop_powerup._name == "Radar" and self._active_shop_powerup._active:
                self._active_shop_powerup.scan_area(self._player._position, board, traps)
                    
                        
            # Handle recall usage
            # Press r for the first time - place recall
            # Press r when recall was placed - teleport to recall
            if keyboard_utils.check_key_event(key_event, 'r') and self._active_shop_powerup._active and self._active_shop_powerup._name == "Recall":
                if self._active_shop_powerup._placed and len(self._active_shop_powerup._previous_positions) != 0:
                    self._active_shop_powerup.recall(self._player._entity, self._player._position, board)
                    occupied_positions.remove(self._active_shop_powerup._position)
                    show_state = True
                elif len(self._active_shop_powerup._previous_positions) > 1:
                    self._active_shop_powerup.place(board, occupied_positions)
                    occupied_positions.append(self._active_shop_powerup._position)
                    show_state = True


            # Handle eating snack
            if self._player._position == self._current_snack._position:
                if recon_start_reached:
                    self._recon_snack._eaten_counter += 1
                
                if self._active_shop_powerup._name == "Doubler" and self._active_shop_powerup._active:
                    self._active_shop_powerup.double_points(self._snack, self._current_snack)
                else:
                    self._snack.eat_snack(current_level_index, self._current_snack)
                
                occupied_positions.remove(self._current_snack._position)
                self._game_utils.set_snack_eaten(self._current_snack._type)

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
                self._recon_snack.reveal_position(board, traps)
                self._game_utils._traps_revealed = True
                occupied_positions.remove(self._recon_snack._position)
            
            # Handle player eating any trap
            trap = next((t for t in traps if t._position == self._player._position), None)
            if trap:
                # Check type and activate accordingly
                match trap._type:
                    case 'hunger': 
                        occupied_positions.remove(trap._position)
                        trap.reduce_snack_count(board, occupied_positions)
                        occupied_positions.append(trap._position)
                        self._game_utils._hunger_trap_eaten = True
                    case 'parallel dimension': 
                        self.activate_parallel_trap(trap, game_mode)
                        traps.remove(trap)
                        occupied_positions.remove(trap._position)
                        self._game_utils._parallel_trap_eaten = True
                    case _: print("No type found")                
        
        self.clear_owned_items(game_mode, current_level_index)
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

        if self._account._name == "":
            self.menu.prompt_name()
        else:
            print(f"Welcome back {self._account._name}!")

        # Main menu loop
        while True:
            if show_menu:
                self._menu_front.print_game_menu(consts.VERSION, self._main_menu_options)
                show_menu = False

            key_event = keyboard.read_event(suppress=True)

            if keyboard_utils.check_key_event(key_event, self._main_menu_options[0]):
                self.menu.mode_selection_menu(self._classic_levels)
                show_menu = True
            elif keyboard_utils.check_key_event(key_event, self._main_menu_options[1]):
                self.menu.shop_menu()
                show_menu = True
            elif keyboard_utils.check_key_event(key_event, self._main_menu_options[2]):
                print("entering account")
                self._account.account_display()
                show_menu = True
            elif keyboard_utils.check_key_event(key_event, self._main_menu_options[3]):
                self.menu.game_options(self._classic_levels, self._save_file)
                show_menu = True
            elif keyboard_utils.check_key_event(key_event, self._main_menu_options[4]):
                self.menu.version_log()
                show_menu = True
            elif keyboard_utils.check_key_event(key_event, self._main_menu_options[5]):
                break
        
        self._save_file.save_prompt(key_event, self._classic_levels) if not self._save_file._already_saved else None
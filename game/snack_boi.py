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
from assets.position.position2d import Position2D
from assets.menu_front import MenuFront
from account.account import Account
from assets.levels.levels_set import levels_set
from assets.shop.shop_item import ShopItem
from assets.shop.shop_items import ShopItems
from assets.enums.enums import MainMenuOptions, MovementKeys, Gamemodes, MiscGameControls, SnackTypes
from boards.board import Board
from utils.consts import EMPTY_SHOP_ITEM, PLAYER_ENTITY
from utils import terminal_clearing


# Game class where the game logic is implemented
class Game:    
    # Player and snack related properties
    _player: Player = Player(PLAYER_ENTITY)
    _snack: Snack = Snack()
    _normal_snack: NormalSnack = NormalSnack()
    _super_snack: SuperSnack = SuperSnack()
    _fake_snack: FakeSnack = FakeSnack()
    _current_snack: Snack = Snack()
    
    # Powerup related properties
    _recon_snack: ReconSnack = ReconSnack()

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
        if game_mode == "classic" and self._snack._count >= levels_set.get_at(current_level_index)._win_cap and (self._active_shop_powerup.reached_usage_per_game() or self._active_shop_powerup._active):
            self._active_shop_powerup.complete_usage()
        elif game_mode == "endless" and self._active_shop_powerup.reached_usage_per_game():
            self._active_shop_powerup.complete_usage()

        self._active_shop_powerup.reset()

        # Update with used powerup and erase ones with zero quantity
        self._account._owned_shop_items = ShopItems([self._active_shop_powerup if self._active_shop_powerup._name == powerup._name else powerup for powerup in self._account._owned_shop_items.get_items()])
        self._account._owned_shop_items = ShopItems([powerup for powerup in self._account._owned_shop_items.get_items() if powerup._stock > 0])

    def game_spawn_snack(self, board: Board, occupied_positions: List[Position2D], snack_type: SnackTypes) -> None:
        '''
            Spawns snack based on the snack number generated on the board 
        '''
        match snack_type:
            case SnackTypes.NORMAL:
                self._normal_snack.spawn(board, occupied_positions)
                self._current_snack = self._normal_snack
            case SnackTypes.FAKE:
                self._fake_snack.spawn(board, occupied_positions)
                self._current_snack = self._fake_snack
            case SnackTypes.SUPER:
                self._super_snack.spawn(board, occupied_positions)
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
        key_event: KeyboardEvent
        show_state: bool = True
        intro_show_state: bool = True
        recon_duration: int = self._recon_snack._duration
        random_snack_type: SnackTypes
        trap: Trap | None
        occupied_positions: List[Position2D] = []
        levels_unlocked: int = 0
        hunger_traps: List[Trap] = []
        parallel_dimension_traps: List[Trap] = []
        traps: List[Trap] = []
        
        owned_powerups: List[ShopItem] = self._account._owned_shop_items.get_items()
        powerup_index: int

        # Eating flags for one time display
        recon_start_reached: bool = False

        for level in levels_set.get_items():
            if level._selected:
                break
            current_level_index += 1
        
        # Game setup
        self._player.spawn(board)
        
        # Add new snack logic available starting from certain levels
        if current_level_index >= consts.NEW_SNACKS_START_LVL-1:
            random_snack_type = random.choice(list(SnackTypes))
            self.game_spawn_snack(board, occupied_positions, random_snack_type)
            occupied_positions.append(self._current_snack._position)
        else:
            self._normal_snack.spawn(board, occupied_positions)
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
                trap.spawn(board, occupied_positions)
                occupied_positions.append(trap._position)
            
            recon_start_reached = True
        
        levels_unlocked = len([lvl for lvl in levels_set.get_items() if lvl._unlocked == True])

        # Prompt user to choose a powerup if they have any
        if owned_powerups:
            powerup_index = self.menu.prompt_powerup_selection(owned_powerups)
            if powerup_index >= 0:
                self._active_shop_powerup = owned_powerups[powerup_index]
        
        # Start precording positions for recall gadget
        if self._active_shop_powerup._name == "Recall":
            self._active_shop_powerup.record_last_position(self._player._position)

        # Game loop handling both modes
        while True:
            # Intro text before game display
            if intro_show_state and game_mode == Gamemodes.CLASSIC.value:
                self._game_utils.intro_text_display(levels_unlocked, current_level_index)
                intro_show_state = False
            
            # Handle win condition
            if game_mode == Gamemodes.CLASSIC.value and self._snack._count >= levels_set.get_at(current_level_index)._win_cap:
                self._game_utils.classic_game_win(current_level_index, levels_set.get_items(), self._account)
                break
            

            if show_state:
                terminal_clearing.clear_terminal()
                self._game_utils.display_current_state(board, current_level_index, 
                                                       levels_set.get_items(), 
                                                       game_mode, self._current_snack._type, 
                                                       recon_duration, self._recon_snack._active,
                                                       self._active_shop_powerup)
                
                # Object tracker for debugging purposes
                # debug.print_obj_tracker(occupied_positions, self._current_snack, traps, self._recon_snack)
                show_state = False            

            key_event = keyboard.read_event(suppress=True)

            if keyboard_utils.check_key_event(key_event, MiscGameControls.QUIT.value):
                break

            # Toggle active powerup
            if keyboard_utils.check_key_event(key_event, MiscGameControls.USE_POWERUP.value) and not self._active_shop_powerup._active and not self._active_shop_powerup.reached_usage_per_game():
                self._active_shop_powerup.activate()
                show_state = True
            

            if key_event.event_type == keyboard.KEY_DOWN and key_event.name in MovementKeys._value2member_map_:
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
                    self._active_shop_powerup.record_last_position(self._player._position)

                    # Handle maintaining unit 
                    if self._player._position != self._active_shop_powerup.get_position() and self._active_shop_powerup._placed:
                        board.set(self._active_shop_powerup._position.x, self._active_shop_powerup._position.y, self._active_shop_powerup._entity)

            # Handle area scan
            if self._active_shop_powerup._name == "Radar" and self._active_shop_powerup._active:
                self._active_shop_powerup.scan_area(self._player._position, board, traps)
                if board.at(self._player._position.x, self._player._position.y) == ' ':
                    board.set(self._player._position.x, self._player._position.y, self._player._entity)
                    
                        
            # Handle recall usage
            # Press r for the first time - place recall
            # Press r when recall was placed - teleport to recall
            if keyboard_utils.check_key_event(key_event, MiscGameControls.USE_RECALL.value) and self._active_shop_powerup._active and self._active_shop_powerup._name == "Recall":
                if self._active_shop_powerup._placed and len(self._active_shop_powerup._previous_positions) != 0:
                    self._active_shop_powerup.record_last_position(self._player._position)
                    self._active_shop_powerup.recall(self._player._entity, self._player._position, board)
                    self._active_shop_powerup.record_last_position(self._player._position)
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
                    random_snack_type = random.choice(list(SnackTypes))
                    self.game_spawn_snack(board, occupied_positions, random_snack_type)
                    occupied_positions.append(self._current_snack._position)
                else:
                    self._normal_snack.spawn(board, occupied_positions)
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
        self._save_file.load(levels_set.get_items())

        if self._account._name == "":
            self.menu.prompt_name()
        else:
            print(f"Welcome back {self._account._name}!")

        # Main menu loop
        while True:
            if show_menu:
                terminal_clearing.clear_terminal()
                self._menu_front.print_game_menu()
                show_menu = False

            key_event = keyboard.read_event(suppress=True)

            if keyboard_utils.check_key_event(key_event, MainMenuOptions.START_GAME.value):
                self.menu.mode_selection_menu(levels_set.get_items())
                show_menu = True
            elif keyboard_utils.check_key_event(key_event, MainMenuOptions.SHOP_MENU.value):
                self.menu.shop_menu()
                show_menu = True
            elif keyboard_utils.check_key_event(key_event, MainMenuOptions.ACCOUNT.value):
                self._account.account_display()
                show_menu = True
            elif keyboard_utils.check_key_event(key_event, MainMenuOptions.OPTIONS.value):
                self.menu.game_options(levels_set.get_items(), self._save_file)
                show_menu = True
            elif keyboard_utils.check_key_event(key_event, MainMenuOptions.VERSION_LOG.value):
                self.menu.version_log()
                show_menu = True
            elif keyboard_utils.check_key_event(key_event, MainMenuOptions.QUIT.value):
                break
        
        self._save_file.save_prompt(key_event, levels_set.get_items()) if not self._save_file._already_saved else None
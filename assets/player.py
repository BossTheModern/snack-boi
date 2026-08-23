'''
    player.py

    Player module handling player logic (spawn, movement)
'''
from utils import keyboard_utils
from boards.board import Board
import random
import keyboard
from keyboard import KeyboardEvent
from assets.position.position2d import Position2D
from assets.enums.enums import MovementKeys
from assets.spawnable.spawnable import Spawnable

class Player(Spawnable):
    _parallel_position: Position2D = Position2D()

    def spawn(self, board: Board) -> None:
        super().spawn(board)
        board.set(self._position.x, self._position.y, self._entity)

    def spawn_player(self, board: Board, obstacle_char: str) -> None:
        '''
            Spawns player on the grid ensuring there are no obstacles on
            the way

            NOTE: Because it only checks for obstacles upon spawning, it
                  must be used first before spawning anything else once
                  the game starts
        '''
        random_x: int = random.randint(0, board._width-1)
        random_y: int = random.randint(0, board._height-1)
        self._position.set(random_x, random_y)
        
        while board.at(self._position.x, self._position.y) == obstacle_char:
            random_x = random.randint(0, board._width-1)
            random_y = random.randint(0, board._height-1)
            self._position.set(random_x, random_y) 
        
        board.set(self._position.x, self._position.y, self._entity)
    
    def parallel_spawn_player(self, board: Board) -> None:
        '''
            Spawns player on the parallel dimension upon activating 
            parallel dimension trap
        '''
        self._parallel_position.set(random.randint(0, board._width-1), random.randint(0, board._height-1))
        board.set(self._parallel_position.x, self._parallel_position.y, self._entity)

    def parallell_despawn_player(self, board: Board) -> None:
        '''
            Despawns player from the parallell dimension,
            used upon exiting the dimension
        '''
        board.set(self._parallel_position.x, self._parallel_position.y, ' ')
        self._parallel_position.clear()
    
    def move_player(self, move_input: KeyboardEvent, board: Board, obstacle_char: str, player_pos: Position2D) -> None:
        '''
            Handles player movement on the board ensuring the player does not
            go outside the board nor stepping on top of obstacles
        '''
        if keyboard_utils.check_key_event(move_input, MovementKeys.UP.value):
            if (player_pos.y - 1 < 0):
                print("Out of bounds, try again")
                move_input = keyboard.read_event(suppress=True)
            elif board.at(player_pos.x, player_pos.y-1) == obstacle_char:
                print("Obstacle in the way, try again")
                move_input = keyboard.read_event(suppress=True)
            else:
                board.set(player_pos.x, player_pos.y, ' ')
                player_pos.move_up()
                board.set(player_pos.x, player_pos.y, self._entity)
        elif keyboard_utils.check_key_event(move_input, MovementKeys.LEFT.value):
            if (player_pos.x - 1 < 0):
                print("Out of bounds, try again")
                move_input = keyboard.read_event(suppress=True)
            elif board.at(player_pos.x-1, player_pos.y) == obstacle_char:
                print("Obstacle in the way, try again")
                move_input = keyboard.read_event(suppress=True)
            else:
                board.set(player_pos.x, player_pos.y, ' ')
                player_pos.move_left()
                board.set(player_pos.x, player_pos.y, self._entity)
        elif keyboard_utils.check_key_event(move_input, MovementKeys.DOWN.value):
            if (player_pos.y + 1 > board._height-1):
                print("Out of bounds, try again")
                move_input = keyboard.read_event(suppress=True)
            elif board.at(player_pos.x, player_pos.y+1) == obstacle_char:
                print("Obstacle in the way, try again")
                move_input = keyboard.read_event(suppress=True)
            else:
                board.set(player_pos.x, player_pos.y, ' ')
                player_pos.move_down()
                board.set(player_pos.x, player_pos.y, self._entity)
        elif keyboard_utils.check_key_event(move_input, MovementKeys.RIGHT.value):
            if (player_pos.x + 1 > board._width-1):
                print("Out of bounds, try again")
                move_input = keyboard.read_event(suppress=True)
            elif board.at(player_pos.x+1, player_pos.y) == obstacle_char:
                print("Obstacle in the way, try again")
                move_input = keyboard.read_event(suppress=True)
            else:
                board.set(player_pos.x, player_pos.y, ' ')
                player_pos.move_right()
                board.set(player_pos.x, player_pos.y, self._entity)
    
    def clear_data(self) -> None:
        '''
            Clears player data
        '''
        self._position.clear()
        self._parallel_position.clear()
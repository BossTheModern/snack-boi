'''
    player.py

    Player module handling player logic (spawn, movement)
'''
from typing import List
from utils import keyboard_utils
import random
import keyboard
from keyboard import KeyboardEvent

class Player:
    _entity: str = 'O'
    _position: List[int] = [0, 0]
    _parallel_position: List[int] = [0, 0]

    def spawn_player(self, grid: List[List[str]], obstacle_char: str) -> None:
        '''
            Spawns player on the grid ensuring there are no obstacles on
            the way

            NOTE: Because it only checks for obstacles upon spawning, it
                  must be used first before spawning anything else once
                  the game starts
        '''
        self._position = [random.randint(0, len(grid)-1), random.randint(0, len(grid)-1)]
        
        while grid[self._position[0]][self._position[1]] == obstacle_char:
            self._position = [random.randint(0, len(grid)-1), random.randint(0, len(grid)-1)] 
        
        grid[self._position[0]][self._position[1]] = self._entity
    
    def parallel_spawn_player(self, grid: List[List[str]]) -> None:
        '''
            Spawns player on the parallel dimension upon activating 
            parallel dimension trap
        '''
        self._parallel_position = [random.randint(0, len(grid)-1), random.randint(0, len(grid)-1)]
        grid[self._parallel_position[0]][self._parallel_position[1]] = self._entity
    
    def move_player(self, move_input: KeyboardEvent, grid: List[List[str]], obstacle_char: str, player_pos: List[int]) -> None:
        '''
            Handles player movement on the board ensuring the player does not
            go outside the board nor stepping on top of obstacles
        '''
        if keyboard_utils.check_key_event(move_input, 'w'):
            if (player_pos[0] - 1 < 0):
                print("Out of bounds, try again")
                move_input = keyboard.read_event(suppress=True)
            elif grid[player_pos[0]-1][player_pos[1]] == obstacle_char:
                print("Obstacle in the way, try again")
                move_input = keyboard.read_event(suppress=True)
            else:
                grid[player_pos[0]][player_pos[1]] = ' '
                player_pos[0] -= 1
                grid[player_pos[0]][player_pos[1]] = self._entity
        elif keyboard_utils.check_key_event(move_input, 'a'):
            if (player_pos[1] - 1 < 0):
                print("Out of bounds, try again")
                move_input = keyboard.read_event(suppress=True)
            elif grid[player_pos[0]][player_pos[1]-1] == obstacle_char:
                print("Obstacle in the way, try again")
                move_input = keyboard.read_event(suppress=True)
            else:
                grid[player_pos[0]][player_pos[1]] = ' '
                player_pos[1] -= 1
                grid[player_pos[0]][player_pos[1]] = self._entity
        elif keyboard_utils.check_key_event(move_input, 's'):
            if (player_pos[0] + 1 > len(grid)-1):
                print("Out of bounds, try again")
                move_input = keyboard.read_event(suppress=True)
            elif grid[player_pos[0]+1][player_pos[1]] == obstacle_char:
                print("Obstacle in the way, try again")
                move_input = keyboard.read_event(suppress=True)
            else:
                grid[player_pos[0]][player_pos[1]] = ' '
                player_pos[0] += 1
                grid[player_pos[0]][player_pos[1]] = self._entity
        elif keyboard_utils.check_key_event(move_input, 'd'):
            if (player_pos[1] + 1 > len(grid)-1):
                print("Out of bounds, try again")
                move_input = keyboard.read_event(suppress=True)
            elif grid[player_pos[0]][player_pos[1]+1] == obstacle_char:
                print("Obstacle in the way, try again")
                move_input = keyboard.read_event(suppress=True)
            else:
                grid[player_pos[0]][player_pos[1]] = ' '
                player_pos[1] += 1
                grid[player_pos[0]][player_pos[1]] = self._entity
    
    def clear_data(self) -> None:
        '''
            Clears player data
        '''
        self._position.clear()
        self._parallel_position.clear()
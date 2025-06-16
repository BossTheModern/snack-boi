# Player module with related player data and movement handling
from typing import List
import random
import keyboard
from keyboard import KeyboardEvent

class Player:
    _entity: str = 'O'
    _position: List[int] = [0, 0]
    _parallel_position: List[int] = [0, 0]

    def check_key_event(self, key_event: KeyboardEvent, target_key: str):
        return key_event.event_type == keyboard.KEY_DOWN and key_event.name == target_key
    
    def spawn_player(self, grid: List[List[str]], obstacle_char: str) -> None:
        self._position = [random.randint(0, len(grid)-1), random.randint(0, len(grid)-1)]
        
        while grid[self._position[0]][self._position[1]] == obstacle_char:
            #print("Player spawn position is an obstacle, rerolling player position")
            self._position = [random.randint(0, len(grid)-1), random.randint(0, len(grid)-1)] 
        
        grid[self._position[0]][self._position[1]] = self._entity
    
    def parallel_spawn_player(self, grid: List[List[str]]) -> None:
        self._parallel_position = [random.randint(0, len(grid)-1), random.randint(0, len(grid)-1)]
        grid[self._parallel_position[0]][self._parallel_position[1]] = self._entity
    
    def move_player(self, move_input: KeyboardEvent, grid: List[List[str]], obstacle_char: str, player_pos: List[int]) -> None:
        if self.check_key_event(move_input, 'w'):
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
        elif self.check_key_event(move_input, 'a'):
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
        elif self.check_key_event(move_input, 's'):
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
        elif self.check_key_event(move_input, 'd'):
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
'''
    recall.py

    Handles logic for recall
'''
from assets.shop.shop_item import ShopItem
from  utils.consts import SHOP_ITEM_LIMIT
from typing import List
import textwrap


class Recall(ShopItem):
    def __init__(self) -> None:
        super().__init__('Recall', 20, textwrap.fill('Place it on the map and teleport back to it', width=50), SHOP_ITEM_LIMIT)
        self._active: bool = False
        self._duration: int = 3 # Duration in number of snacks eaten
        self._active_duration: int = 0
        self._use_limit: int = 1 
        self._use_count: int = 0

        self._previous_positions: List[List[int]] = []
        self._position: List[int] = []
        self._entity: str = 'R'
        self._placed: bool = False

    def place(self, board: List[List[int]], occupied_positions: List[List[int]]) -> None:
        '''
            places recall item at the last recorded position
            the player was in given the position is not occupied
            by anything else

            can also be used to maintain placement when player leaves 
            recall's position
        '''    
        self._position = self._previous_positions[0]

        if self._position in occupied_positions:
            print("Something is preventing you from placing the recall")
        else:
            board[self._position[0]][self._position[1]] = self._entity
            self._placed = True

    def prerecord_last_positions(self, position: List[int]) -> None:
        '''
            Adds positions to record. Used until there are two
            positions recorded
        '''
        if position not in self._previous_positions:
            self._previous_positions.append(position.copy())
            self._previous_positions.reverse()
    
    def record_last_positions(self, position: List[int], tracked_positions: List[List[int]]) -> None:
        '''
            records last position the player was in        
        '''
        first_tracked_position: List[int] = tracked_positions[0]
        all_elements_same: bool = all(position == first_tracked_position for position in tracked_positions[1:])

        if position not in self._previous_positions or not all_elements_same:
            self._previous_positions.reverse()
            self._previous_positions[1] = position.copy()

    def recall(self, player_entity: str, current_position: List[int], board: List[List[int]]) -> None:
        '''
            teleports player to given position
        '''
        print("teleporting")
        print(current_position)
        board[current_position[0]][current_position[1]] = ' '
        board[self._position[0]][self._position[1]] = player_entity
        current_position[0] = self._position[0]
        current_position[1] = self._position[1]
        self._position.clear()
        self._placed = False

        self._active_duration -= 1 
        if self._active_duration == 0:
            self.deactivate()
                   

    def activate(self) -> None:
        '''
            Activates recall effect        
        '''
        if self.reached_usage_per_game():
            print(f"Maximum number of uses per game ({self._use_limit}) reached.")
        else:
            self._active = True
            self._active_duration = self._duration
    
    def deactivate(self) -> None:
        self._active = False
        self._use_count += 1
    
    def reset(self) -> None:
        self._use_count = 0
        self._active_duration = 0
        self._active = False
        self._previous_positions.clear()
        self._position.clear()
        self._placed = False
    
    def reached_usage_per_game(self) -> bool:
        return self._use_count == self._use_limit
    
    def complete_usage(self) -> None:
        self._stock -= 1

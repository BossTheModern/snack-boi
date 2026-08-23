'''
    recall.py

    Handles logic for recall
'''
from assets.shop.shop_item import ShopItem
from assets.position.position2d import Position2D
from utils.queue import Queue
from utils.consts import SHOP_ITEM_LIMIT
from boards.board import Board
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

        self._previous_positions: Queue = Queue(2)
        self._position: Position2D = Position2D()
        self._entity: str = 'R'
        self._placed: bool = False

    def place(self, board: Board, occupied_positions: List[Position2D]) -> None:
        '''
            places recall item at the last recorded position
            the player was in given the position is not occupied
            by anything else

            can also be used to maintain placement when player leaves 
            recall's position
        '''    
        self._position = self.get_last_position()

        print("position: ", self._position.x, self._position.y)

        if self._position.is_in(occupied_positions):
            print("Something is preventing you from placing the recall")
        else:
            board.set(self._position.x, self._position.y, self._entity)
            self._placed = True

    def record_last_position(self, position: Position2D) -> None:
        new_record: Position2D = Position2D(position.x, position.y)

        if self._previous_positions.is_full():
            print("shuffling record")
            self._previous_positions.dequeue()

        self._previous_positions.enqueue(new_record)
        print(f"length previous positions: {len(self._previous_positions)}")

    def get_last_position(self) -> Position2D:
        return self._previous_positions.peek()

    def get_position(self) -> Position2D:
        return self._position

    def recall(self, player_entity: str, current_position: Position2D, board: Board) -> None:
        '''
            teleports player to given position
        '''
        print("teleporting")
        print(current_position)
        board.set(current_position.x, current_position.y, ' ')
        board.set(self._position.x, self._position.y, player_entity)
        current_position.x = self._position.x
        current_position.y = self._position.y
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

'''
    radar.py

    Handles logic for radar powerup
'''
from typing import List
from assets.shop.shop_item import ShopItem
from assets.traps.traps import Trap
from assets.position.position2d import Position2D
from boards.board import Board
from utils.consts import SHOP_ITEM_LIMIT
import textwrap

class Radar(ShopItem):
    def __init__(self) -> None:
        super().__init__('Radar', 15, textwrap.fill('Tell the player if there are traps nearby', width=50), SHOP_ITEM_LIMIT)
        self._active: bool = False
        self._duration: int = 3 # Duration in number of snacks eaten
        self._active_duration: int = 0
        self._use_limit: int = 1 
        self._use_count: int = 0
        self._revealed_traps: List[Trap] = []
        self._trap_not_found_counter: int = 0
        self._counter_limit: int = 2
        self._trap_was_found: bool = False
    
    def coord_is_within_range(self, x: int, y: int, min: int, max: int) -> bool:
        return x >= min and x <= max and y >= min and y <= max
    
    def coord_is_trapped(self, position: Position2D, traps: List[Trap]) -> bool:
        for trap in traps:
            if trap._position == position:
                return True
        return False
    
    def scan_area(self, position: Position2D, board: Board, traps: List[Trap]) -> None:
        '''
            Scans the area around for traps        
        '''
        trap_found: bool = False

        target_area: List[Position2D] = []

        # Clear previously found traps
        if len(self._revealed_traps) > 0:
            for trap in self._revealed_traps:
                trap.hide(board)
            self._revealed_traps.clear()
            
            self._trap_not_found_counter = 0
            self._trap_was_found = True
        
        if self._trap_was_found:
            self._trap_not_found_counter += 1

        if self._trap_not_found_counter == self._counter_limit:
            self._active_duration -= 1
            self._trap_not_found_counter = 0       
            self._trap_was_found = False


        # populate target area coords
        for y in range(position.y-1, position.y+2):
            for x in range(position.x-1, position.x+2):
                if Position2D(x, y) != position and self.coord_is_within_range(x, y, 0, board._width-1):
                    target_area.append(Position2D(x, y))
        
        # iterate through target area coords for objs
        for area_pos in target_area:
            if self.coord_is_trapped(area_pos, traps):

                # reveal trap
                for trap in traps:
                    if trap._position == area_pos:
                        trap.reveal_trap(board)
                        self._revealed_traps.append(trap)

                if not trap_found:
                    trap_found = True
                
        if trap_found:
            print("Trap is nearby")
            trap_found = False

        if self._active_duration == 0:
            # Clear previously found traps
            if len(self._revealed_traps) > 0:
                for trap in self._revealed_traps:
                    trap.hide(board)
                self._revealed_traps.clear()
                    
            self.deactivate()

    def activate(self) -> None:
        '''
            Activates radar effect        
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
        self._revealed_traps = []
        self._trap_not_found_counter = 0
        self._trap_was_found = False
    
    def reached_usage_per_game(self) -> bool:
        return self._use_count == self._use_limit
    
    def complete_usage(self) -> None:
        self._stock -= 1
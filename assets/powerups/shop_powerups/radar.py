'''
    radar.py

    Handles logic for radar powerup
'''
from typing import List
from assets.shop.shop_item import ShopItem
from assets.traps.traps import Trap
from utils.consts import SHOP_ITEM_LIMIT
from utils.consts import NON_TRAP_TILE_CONTENT
import textwrap

class Radar(ShopItem):
    def __init__(self) -> None:
        super().__init__('Radar', 15, textwrap.fill('Tell the player if a trap is nearby', width=40), SHOP_ITEM_LIMIT)
        self._active: bool = False
        self._duration: int = 3 # Duration in number of snacks eaten
        self._active_duration: int = 0
        self._use_limit: int = 1 
        self._use_count: int = 0
        self._revealed_traps: List[Trap] = []
        self._trap_not_found_counter: int = 0
        self._counter_limit: int = 2
    
    def coord_is_within_range(self, x: int, y: int, min: int, max: int) -> bool:
        return x >= min and x <= max and y >= min and y <= max
    
    def coord_is_trapped(self, position: List[int], traps: List[Trap]) -> bool:
        for trap in traps:
            if trap._position == position:
                return True
        return False
    
    def scan_area(self, position: List[int], board: List[List[str]], traps: List[Trap]) -> None:
        '''
            Scans the area around for traps        
        '''
        trap_found: bool = False

        target_area: List[List[int]] = []

        # Clear previously found traps
        if len(self._revealed_traps) > 0:
            for trap in self._revealed_traps:
                trap.hide(board)
            self._revealed_traps.clear()
            
            self._trap_not_found_counter = 0
        else:
            self._trap_not_found_counter += 1

        if self._trap_not_found_counter == self._counter_limit:
            self._active_duration -= 1       

        # populate target area coords
        for y in range(position[0]-1, position[0]+2):
            for x in range(position[1]-1, position[1]+2):
                if [y, x] != position and self.coord_is_within_range(x, y, 0, len(board[0])-1):
                    target_area.append([y, x])
        
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
    
    def reached_usage_per_game(self) -> bool:
        return self._use_count == self._use_limit
    
    def complete_usage(self) -> None:
        self._stock -= 1
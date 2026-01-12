'''
    doubler.py

    Handles logic for doubler powerup
'''
from assets.shop.shop_item import ShopItem
from utils.consts import SHOP_ITEM_LIMIT
from assets.snacks.snack import Snack
from utils.consts import NORMAL_SNACK_POINTS
from utils.consts import SUPER_SNACK_POINTS
import textwrap


class Doubler(ShopItem):
    def __init__(self) -> None:
        super().__init__('Doubler', 10, textwrap.fill('Doubles points earned from eating snacks', width=40), SHOP_ITEM_LIMIT)
        self._active: bool = False
        self._duration: int = 3 # Duration in number of snacks eaten
        self._active_duration: int = 0
        self._use_limit: int = 1 
        self._use_count: int = 0
    
    def double_points(self, snack: Snack, current_snack: Snack) -> None:
        '''
            Activates doubler effect: doubles points earned from eating snacks
            for a cerayin duration of snacks eaten
        '''
        if self._active_duration > 0:
            match current_snack._type:
                case 'normal': 
                    snack._count += 2 * NORMAL_SNACK_POINTS
                    self._active_duration -= 1
                case 'super': 
                    snack._count += 2 * SUPER_SNACK_POINTS
                    self._active_duration -= 1

            
            if self._active_duration == 0:
                self.deactivate()

    def activate(self) -> None:
        '''
            Activates doubler effect
        '''
        if self.reached_usage_per_game():
            print(f"Maximum number of uses per game ({self._use_limit}) reached.")
        else:
            self._active = True
            self._active_duration = self._duration
    
    def deactivate(self) -> None:
        '''
            Deactivates doubler effect
        '''
        self._active = False
        self._use_count += 1
    
    def reset(self) -> None:
        self._use_count = 0
        self._active_duration = 0
        self._active = False
    
    def reached_usage_per_game(self) -> bool:
        return self._use_count == self._use_limit
    
    def complete_usage(self) -> None:
        self._stock -= 1

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
    
    def activate(self, snack: Snack, current_snack: Snack) -> None:
        '''
            Activates doubler effect: doubles points earned from eating snacks
            for a cerayin duration of snacks eaten
        '''
        match current_snack._type:
            case 'normal': snack._count += 2 * NORMAL_SNACK_POINTS
            case 'super': snack._count += 2 * SUPER_SNACK_POINTS

    
    def deactivate(self) -> None:
        '''
            Deactivates doubler effect
        '''
        self._active = False

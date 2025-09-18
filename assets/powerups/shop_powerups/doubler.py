'''
    doubler.py

    Handles logic for doubler powerup
'''
from assets.shop.shop_item import ShopItem
from utils.consts import SHOP_ITEM_LIMIT
import textwrap


class Doubler(ShopItem):
    def __init__(self) -> None:
        super().__init__('Doubler', 10, textwrap.fill('Doubles points earned from eating snacks', width=40), SHOP_ITEM_LIMIT)
        self._active: bool = False
        self._duration: int = 3 # Duration in number of snacks eaten
    
    def activate(self) -> None:
        '''
            Activates doubler effect: doubles points earned from eating snacks
            for a cerayin duration of snacks eaten
        '''
        self._active = True
    
    def deactivate(self) -> None:
        '''
            Deactivates doubler effect
        '''
        self._active = False

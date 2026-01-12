'''
    shop_items.py

    Shop items module
'''

from assets.shop.shop_item import ShopItem
from assets.powerups.shop_powerups.doubler import Doubler
from assets.powerups.shop_powerups.radar import Radar
from assets.powerups.shop_powerups.recall import Recall 
from typing import List

class ShopItems:
    _shop_items: List[ShopItem] = [
        Doubler(),
        Radar(),
        Recall(),
    ]
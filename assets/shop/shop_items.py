'''
    shop_items.py

    Shop items module
'''

from assets.shop.shop_item import ShopItem
from assets.powerups.shop_powerups.doubler import Doubler
from assets.powerups.shop_powerups.radar import Radar
from utils.consts import SHOP_ITEM_LIMIT
from typing import List
import textwrap

class ShopItems:
    _shop_items: List[ShopItem] = [
        Doubler(),
        Radar(),
        ShopItem('Recall', 20, textwrap.fill('Place it on the map and teleport back to it', width=40), SHOP_ITEM_LIMIT)
    ]
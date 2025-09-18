'''
    shop_items.py

    Shop items module
'''

from assets.shop.shop_item import ShopItem
from assets.powerups.shop_powerups.doubler import Doubler
from utils.consts import SHOP_ITEM_LIMIT
from typing import List
import textwrap

class ShopItems:
    _shop_items: List[ShopItem] = [
        Doubler(),
        ShopItem('Radar', 15, textwrap.fill('Tell the player if a trap is nearby', width=40), SHOP_ITEM_LIMIT),
        ShopItem('Recall', 20, textwrap.fill('Place it on the map and teleport back to it', width=40), SHOP_ITEM_LIMIT)
    ]
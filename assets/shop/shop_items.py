'''
    shop_items.py

    Shop items module
'''

from assets.shop.shop_item import ShopItem
from assets.powerups.shop_powerups.doubler import Doubler
from assets.powerups.shop_powerups.radar import Radar
from assets.powerups.shop_powerups.recall import Recall 
from typing import List
import textwrap
from utils.consts import SHOP_ITEM_LIMIT


class ShopItems:
    _shop_items: List[ShopItem] = [
        Doubler(),
        Radar(),
        Recall(),
        ShopItem("Test item 4", 4, textwrap.fill('Desc item 4', width=40), SHOP_ITEM_LIMIT),
        ShopItem("Test item 5", 5, textwrap.fill('Desc item 5', width=40), SHOP_ITEM_LIMIT),
        ShopItem("Test item 6", 6, textwrap.fill('Desc item 6', width=40), SHOP_ITEM_LIMIT),
        ShopItem("Test item 7", 7, textwrap.fill('Desc item 7', width=40), SHOP_ITEM_LIMIT),
    ]
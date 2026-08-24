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
    def __init__(self, items: List[ShopItem] = []) -> None:
        self._items: List[ShopItem] = items

    def get_items(self) -> List[ShopItem]:
        return self._items

    def size(self) -> int:
        return len(self._items)

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def add_item(self, item: ShopItem) -> None:
        self._items.append(item)

    def clear_items(self) -> None:
        self._items.clear() 
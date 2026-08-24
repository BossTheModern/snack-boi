'''
    shop_items_collection.py

    Collection containing shop items
'''

from assets.shop.shop_items import ShopItems
from assets.shop.shop_item import ShopItem
from assets.powerups.shop_powerups.doubler import Doubler
from assets.powerups.shop_powerups.radar import Radar
from assets.powerups.shop_powerups.recall import Recall 
import textwrap
from utils.consts import SHOP_ITEM_LIMIT

shop_item_collection: ShopItems = ShopItems([
    Doubler(),
    Radar(),
    Recall(),
    ShopItem("Test item 4", 4, textwrap.fill('Desc item 4', width=40), SHOP_ITEM_LIMIT),
    ShopItem("Test item 5", 5, textwrap.fill('Desc item 5', width=40), SHOP_ITEM_LIMIT),
    ShopItem("Test item 6", 6, textwrap.fill('Desc item 6', width=40), SHOP_ITEM_LIMIT),
    ShopItem("Test item 7", 7, textwrap.fill('Desc item 7', width=40), SHOP_ITEM_LIMIT),
])
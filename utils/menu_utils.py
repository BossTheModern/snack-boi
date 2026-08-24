'''
    menu_utils.py

    collection of menu related helper functions
'''
from typing import List
from assets.shop.shop_items import ShopItems
from utils.consts import PAGE_SIZE

def make_pages(items: ShopItems) -> List[ShopItems]:
    pages: List[ShopItems] = []
    page: ShopItems = ShopItems()

    for index, item in enumerate(items.get_items()):
        page.add_item(item)

        if page.size() == PAGE_SIZE or index == items.size()-1:
            pages.append(ShopItems(page.get_items().copy()))
            page.clear_items()

    return pages

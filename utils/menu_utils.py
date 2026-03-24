'''
    menu_utils.py

    collection of menu related helper functions
'''
from typing import List
from assets.shop.shop_item import ShopItem
from utils.consts import PAGE_SIZE

def make_pages(items: List[ShopItem]) -> List[List[ShopItem]]:
    pages: List[List[ShopItem]] = []
    page: List[ShopItem] = []

    for index, item in enumerate(items):
        page.append(item)

        if len(page) == PAGE_SIZE or index == len(items)-1:
            pages.append(page.copy())
            page.clear()

    return pages

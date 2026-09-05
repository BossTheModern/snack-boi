'''
    shop_items.py

    Shop items module
'''

from assets.shop.shop_item import ShopItem
from typing import List
from utils.consts import PAGE_SIZE
from assets.collection.collection import Collection

class ShopItems(Collection):
    def __init__(self, items: List[ShopItem] = []) -> None:
        super().__init__(items, page_size = PAGE_SIZE)

    def paginate(self) -> List[ShopItems]:
        pages: List[ShopItems] = []
        page: ShopItems = ShopItems()
        
        for index, item in enumerate(self.get_items()):
            page.add_item(item)
        
            if page.size() == self._page_size or index == self.size()-1:
                pages.append(ShopItems(page.get_items().copy()))
                page.clear_items()
        
        return pages
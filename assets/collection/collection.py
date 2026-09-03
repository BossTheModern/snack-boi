'''
    collection.py

    Collection class for storing a collection of items
    that can be displayed page by page in the menu
'''
from typing import List, Any

class Collection:
    def __init__(self, items: List[Any] = [], page_size: int = 5) -> None:
        self._items: List[Any] = items
        self._page_size: int = page_size

    def get_items(self) -> List[Any]:
        return self._items

    def get_at(self, index: int) -> Any:
        return self._items[index]

    def size(self) -> int:
        return len(self._items)

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def add_item(self, item: Any) -> None:
        self._items.append(item)

    def clear_items(self) -> None:
        self._items.clear()

    def paginate(self) -> List[List[Any]]:
        '''
            returns a list of pages where each page is a list of items
        '''
        page: List[Any] = []
        pages: List[List[Any]] = []

        for item in self._items:
            if len(page) >= self._page_size:
                pages.append(page)
                page = []
            page.append(item)
        if page:
            pages.append(page)
        
        return pages
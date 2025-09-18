'''
    shop_item.py

    Shop item module to handle shop items
'''

class ShopItem:
    def __init__(self, name: str, price: int, description: str, limit: int) -> None:
        self._name: str = name
        self._price: int = price
        self._description: str = description
        self._limit: int = limit
        self._stock: int = 0
    
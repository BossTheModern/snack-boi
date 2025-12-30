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
        self._active: bool = False
    
    def activate(self) -> None:
        pass
    
    def reset(self) -> None:
        pass

    def complete_usage(self) -> None:
        pass

    def reached_usage_per_game(self) -> bool:
        pass
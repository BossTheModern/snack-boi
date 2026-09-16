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
        self._use_count: int = 0
        self._use_limit: int = 1
        self._active_duration: int = 0
        self._active: bool = False
        self._duration: int = 3 # Standard duration of number of triggers
    
    def activate(self) -> None:
        '''
            Activates recall effect        
        '''
        if self.reached_usage_per_game():
            print(f"Maximum number of uses per game ({self._use_limit}) reached.")
        else:
            self._active = True
            self._active_duration = self._duration

    def deactivate(self) -> None:
        self._active = False
        self._use_count += 1
    
    def reset(self) -> None:
        pass

    def complete_usage(self) -> None:
        self._stock -= 1

    def reduce_duration(self) -> None:
        self._active_duration -= 1

    def reached_usage_per_game(self) -> bool:
        return self._use_count == self._use_limit
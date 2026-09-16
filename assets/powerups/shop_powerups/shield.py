'''
    shield.py

    Shield powerup that protects the player from traps
    When the shield is active, the player can ignore any trap effects
    for a limited number of moves
'''
from assets.shop.shop_item import ShopItem
from utils.consts import SHOP_ITEM_LIMIT

class Shield(ShopItem):
    def __init__(self) -> None:
        super().__init__('Shield', 15, 'Protects you from traps for a limited number of moves', SHOP_ITEM_LIMIT)
        self._duration = 5
        self._used_protection: bool = False
        self._protecting: bool = False

    def is_active(self) -> bool:
        return self._active

    def protect(self) -> None:
        '''
            Reduce the duration upon hitting a trap with shield active
            Accompanied with logic to deactivate the traps
        '''
        self._protecting = True
        self._used_protection = False

    def unprotect(self) -> None:
        self._protecting = False

    def is_protecting(self) -> bool:
        return self._protecting

    def use(self) -> None:
        if self.is_protecting() and not self._used_protection:
            self.reduce_duration()
            self._used_protection = True
        if self._active_duration == 0:
            self.deactivate()

    def reset(self) -> None:
        self._use_count = 0
        self._active_duration = 0
        self._active = False

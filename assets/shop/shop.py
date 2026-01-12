'''
    shop.py

    Shop module handling shop logic 
'''
from typing import List
from assets.shop.shop_item import ShopItem
from assets.shop.shop_items import ShopItems
from account.account import Account

class Shop:
    _shop_items: List[ShopItem] = ShopItems._shop_items

    def print_shop_menu(self, account: Account) -> None:
        '''
            Prints shop menu
        '''
        print(f"{"[SHOP]":-^50}\n")

        # Print names
        for index, item in enumerate(self._shop_items):
            print(f"[{index + 1}] {item._name:<15}", end='')
        
        print()
        
        for item in self._shop_items:
            print(f"Stock: {item._stock}/{item._limit:<10}", end='')

        
        print(f"\n\n{'':-<50}")
        print(f"Balance: {account._points_balance}")
        print("Select item number to view details")
        print("[Q] Back to main menu")

    def show_shop_item_details(self, item_num: int) -> None:
        '''
            Shows detials for a specific shop item

            item_num - number of item in the shop list, not index
        '''
        max_width: int = len('description') + 5
        item_num -= 1

        print(f"{'[ITEM DETAILS]':-^40}")
        print(f"{'Name:':<{max_width}} {self._shop_items[item_num]._name}")
        print(f"{'Description:':<{max_width}} {self._shop_items[item_num]._description}")
        print(f"{'Price:':<{max_width}} {self._shop_items[item_num]._price} points")
        print(f"{'':-<40}\n")
        print("[B] Buy item")
        print("[Q] Back to shop menu")

    def purchase_item_menu(self, item_num: int) -> None:
        '''
            Prompts user to confirm purchase then performs the purchase
        '''
        item_num -= 1

        print(f"{"[NOTICE]":-^40}")
        print(f"Are you sure you want to buy {self._shop_items[item_num]._name}?")
        print(f"{'':-<40}")
        print("[Y] yes [N] no")

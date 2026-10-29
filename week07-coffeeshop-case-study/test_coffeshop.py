from coffeeshop import Beverage, Menu, CoffeeShop

shop = CoffeeShop()

choice = -1

while choice != 0:
    shop.display_app_menu()
    choice = shop.select_from_app_menu()





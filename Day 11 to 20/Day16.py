from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money = MoneyMachine()
maker = CoffeeMaker()

ff = True

while ff:
    opt = menu.get_items()
    ask = input(f"What would you like? ({opt}):")
    if ask == "off":
        ff = False
    elif ask == "report":
        money.report()
        maker.report()
    else:
        drink = menu.find_drink(ask)
        if maker.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                maker.make_coffee(drink)

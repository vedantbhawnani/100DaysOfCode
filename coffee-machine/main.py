from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
items = Menu()
while (1):
    user = input(f"What do you feel like having? ({items.get_items()}) ")
    if user == "99":
        exit()
    elif user == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = items.find_drink(user)

        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)

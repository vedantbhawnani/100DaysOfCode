from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

user = input(f"What do you feel like having?{Menu().get_items}")

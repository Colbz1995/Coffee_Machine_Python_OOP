from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from time import sleep


coffee_machine = CoffeeMaker()
menu = Menu()
money = MoneyMachine()

coffee_machine_on = True

while coffee_machine_on:
    choice = input(f"What would you like?: ({menu.get_items()})")

    if choice == "off":
        coffee_machine_on = False
    elif choice == "report":
        coffee_machine.report()
        money.report()
        sleep(5)
        coffee_machine.clear_screen()
    else:
        drink = menu.find_drink(choice)

        if coffee_machine.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            coffee_machine.make_coffee(drink)
            sleep(5)
            coffee_machine.clear_screen()
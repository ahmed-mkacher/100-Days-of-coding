from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
machine_on = True
while machine_on:
    choice = input(f"What would you like? ({menu.get_items()})")
    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        machine_on = False
    else:
        drink = menu.find_drink(choice)
        if money_machine.make_payment(drink.cost):
            if coffee_maker.is_resource_sufficient(drink):
                coffee_maker.make_coffee(drink)
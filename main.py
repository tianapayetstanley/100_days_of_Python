from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#print report by creating an instance obj of the class MoneyMachine to use method from the class
print("Report on inventory: ")
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
coffee_maker.report()
print()


is_on = True
while is_on:
    options = menu.get_items()
    choice = input(f"what would you like {options}")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
money=0
turn_on=True
my_moneyMachine= MoneyMachine()
my_cofeemaker=CoffeeMaker()
my_menu=Menu()
while turn_on:
    options=my_menu.get_items()
    button_pressed=input(f"What would you like? {options}: ")
    if button_pressed=="off":
        turn_on=False
    elif button_pressed=="report":
        my_moneyMachine.report()
        my_cofeemaker.report()
    else:
        drink=my_menu.find_drink(button_pressed)
        print(drink)
        if my_cofeemaker.is_resource_sufficient(drink):
         
         if my_moneyMachine.make_payment(drink.cost):
            my_cofeemaker.make_coffee(drink)
        #     money_inserted=processCoins()
        
        # if Is_Transaction_successful(money_inserted , drink["cost"]):
        #     if makeDrink(drink["ingredients"]):
        #         print(f"Here is your {button_pressed}. Enjoy! ")
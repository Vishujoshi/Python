from data import resources
from data import MENU
money=0


def is_resource_enough(user_ch):
    for i in user_ch:
        if user_ch[i]>resources[i]:
            print(f"Sorry there is not enough {i}.”")
            return False
    return True

def Is_Transaction_successful(user_money , actual_cost):
    if user_money>=actual_cost:
        global money
        money+=actual_cost
        change=round(user_money-actual_cost,2)
        print(f"Here is your cahnge : {change}$")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def processCoins():
    print("Insert Conins")
    total=int(input("Number Of Quarter coins : "))* 0.25
    total+=int(input("Number Of dimes coins : "))* 0.10
    total+=int(input("Number Of nickels coins : ")) *0.05
    total+=int(input("Number Of pennies coins : ")) *0.01
    return total


def makeDrink(ingrediients):
    for i in ingrediients:
        resources[i]-=ingrediients[i]
    return True

turn_on=True
while turn_on:
    button_pressed=input("What would you like? (espresso/latte/cappuccino): ")
    if button_pressed=="off":
        turn_on=False
    elif button_pressed=="report":
        for i in resources:
            print(f"{i} : {resources[i]}")
        print(f"Money : {money}$")
    else:
        drink=MENU[button_pressed]
        if is_resource_enough(drink["ingredients"]):
            money_inserted=processCoins()
        
        if Is_Transaction_successful(money_inserted , drink["cost"]):
            if makeDrink(drink["ingredients"]):
                print(f"Here is your {button_pressed}. Enjoy! ")
    

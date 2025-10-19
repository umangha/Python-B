from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "coffee": 18,
#         },
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3.0,
#     }
# }

# PROFIT = 0

# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
# }


# def is_resource_sufficient(order_ingredients):
#     '''Takes order ingredients dictionary and return Boolean showing the resource are enough for drink or not'''
#     for item in order_ingredients:
#         # if the ingredients required are more or equal to the 
#         if order_ingredients[item] >= resources[item]:
#             print(f"Sorry there is not enough {item}.")
#             return False
    
#     # When enough resources return True
#     return True

# def process_coins():
#     """Returns the total calculated from coins inserted."""
#     print("Please insert coins.")
#     total = int(input("how many quarters?: ")) * 0.25
#     total += int(input("how many dimes?: ")) * 0.1
#     total += int(input("how many nickles?: ")) * 0.05
#     total += int(input("how many pennies?: ")) * 0.01
#     return total

# def is_transaction_successful(money_received, drink_cost):
#     """Return True when the payment is accepted, or False if money is insufficient."""
#     if money_received >= drink_cost:
#         change = round(money_received - drink_cost,2)
#         print(f"Here is ${change} in change")
#         # Accessing the global variable in local scope
#         global PROFIT
#         PROFIT += drink_cost
#         return True
#     else:
#         print("Soory Not Enough Money. Money Refunded")
#         return False

# def make_coffee(drink_name, order_ingredients):
#     '''Takes drink_name and order ingredients and minuses the order ingredients with machine resources'''
#     for item in order_ingredients:
#         resources[item] -= order_ingredients[item]
#     print(f"Here is your {drink_name}")

# Machine working status
IS_ON = True

# Menu class object
menu=Menu()

# Making a class of for MoneyMachine() which handles the PROFIT report() and make_payment(cost) cost of the drink
machine_money = MoneyMachine()

# Making a object of CoffeeMaker Class
coffee_maker = CoffeeMaker()



while IS_ON:
    choice = input(f"What would you like? {menu.get_items()}: ")
    if choice == "off":
        IS_ON = False
    elif choice == 'report':
        # Prints the current resources of the machine
        coffee_maker.report()

        # print(f"Water: {resources['water']}")
        # print(f"Milk: {resources['milk']}")
        # print(f"Coffee: {resources['coffee']}")

        # Prints the current PROFIT
        machine_money.report()
        # print(f"PROFIT: {PROFIT}")

    else:
        # Searches the drink by name and returns MenuItem Obj
        drink = menu.find_drink(choice)
        ## drink is dictionary holding the ingredients and cost of drink
        # drink = MENU[choice]

        if coffee_maker.is_resource_sufficient(drink):
        # if is_resource_sufficient(drink['ingredients']):

            cost = drink.cost
            # payment = machine_money.process_coins()
            # payment = process_coins()

            # Payment is enough? Check
            if machine_money.make_payment(cost):
            # if is_transaction_successful(payment,drink["cost"]):

                # Make the drink after satisfying all the conditions
                coffee_maker.make_coffee(drink)
                # make_coffee(choice,drink['ingredients'])

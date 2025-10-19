MENU ={
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            # "water": 500,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def compare_resource(resource,req_resource,current_resource):
    '''Takes the Required Rescource(water,milk,coffee) NAME and AMOUNT and Current Machine Resouce AMOUNT and returns the True if there is enough else False'''
    if req_resource > current_resource:
        print(f"Soory there is not enough {resource}.")
        return False
    return True

def process_coins():
    '''Calculates and Returns the Total Money Inserted by user in $'''
    # After Resources check prompt the User to Insert Coin
    # quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
    print("Please insert coins.")
    user_quarters = int(input("How many quarters?: "))
    user_dimes = int(input("How many dimes?: "))
    user_nickles = int(input("How many nickles?: "))
    user_pennies = int(input("How many pennies?: "))
    
    # Rounding of the Float value to 2
    total_money_inserted = round((user_quarters * 0.25) + (user_dimes * 0.10) + (user_nickles * 0.05) + (user_pennies * 0.01),2)
    print(f" You Have Inserted: ${total_money_inserted}")
    return total_money_inserted


def check_resources(drink):
    '''Checks Resources of the user's requested drink to remaining resouces in Machine'''
    try:
        # Returns 'ingredients' and 'cost'
        drink_ingredients = MENU[drink]["ingredients"]

        # Resources required for the drink if the key is not present then return default value of '0'
        req_water = drink_ingredients.get("water",0)
        req_milk = drink_ingredients.get("milk",0)
        req_coffee = drink_ingredients.get("coffee",0)
        # print(f"Required resources for {drink} are:\nWater: {req_water}ml. Milk: {req_milk}ml, Coffee: {req_coffee}g")

        # Compare the drinks required resouces with the current resources of machine
        is_sufficient_water = compare_resource(resource="Water", req_resource=req_water,current_resource=resources["water"])
        is_sufficient_milk = compare_resource(resource="Milk",req_resource=req_milk,current_resource=resources["milk"])
        is_sufficient_coffee = compare_resource(resource="Coffee",req_resource=req_coffee,current_resource=resources["coffee"])

        # Return True if all 3 resources are enough else false
        if is_sufficient_water and is_sufficient_milk and is_sufficient_coffee:
            return True
        # One of the resource is not enough
        return False

    except KeyError:
        # If the drink name doesnot match then dictionary key becomes incorrect
        print("Incorrect drink. Please Enter the drink again")

def check_transaction(total_money,drink_cost,profit):
    '''Takes User inserted total money in $, Cost of the drink and Returns profit'''
    if total_money < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return profit

    profit+=drink_cost
    change_money = total_money-drink_cost
    if change_money > 0:
        print(f"Here is ${change_money} in change.")
    return profit

def deduct_resources(drink):
    '''Deducts the resources required to make the drink from machine current resources'''
    drink_resources = MENU[drink]["ingredients"]

    # subtracting the resources from machine current resources
    for item in drink_resources:
        resources[item] -= drink_resources[item]

def report(profit):
    """Display the current resources and profit."""
    print(
        f"\nCurrent Machine Resources:\n"
        f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${profit}\n"
    )

#######################################################################################

def coffee_machine():
    """MAIN LOGIC OF GAME """
    # Machine earnings
    profit=0
    
    # Status of LOOP
    status= True
    while status:

        # "What would you like? (espresso/latte/cappuccino)" Prompt should repeat
        user_drink = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()

        # "off" is the secret keyword to turn off the machine by maintainence
        if user_drink == 'off':
            # Turn off the machine
            status = False
        elif user_drink == 'report':
            # "report" secret keyword to see the current resources of the machine
            report(profit)
        else: 
            # Check resouces are sufficient
            # Flag to to move forward only if there is enough resource
            resources_status = check_resources(user_drink)

            if resources_status:
                # Function to deduct the ingredients used to make the drink Returns tuple
                deduct_resources(user_drink)

                # Total money inserted by user in $
                total_inserted_money = process_coins()

                # Cost of the drink
                drink_cost = MENU[user_drink]["cost"]

                # Profit of machine updated
                profit = check_transaction(total_money=total_inserted_money, drink_cost=drink_cost,profit=profit)

                # Final print 
                print(f"“Here is your {user_drink}. Enjoy!”.\n")



coffee_machine()
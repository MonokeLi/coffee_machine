MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
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


# TODO: 1. Print report of all coffee resources


def report(money):
    """Returns all the resources inside coffee machine"""
    return f"Water: {resources['water']} \nMilk: {resources['milk']} \nCoffee: {resources['coffee']} \nMoney: ${money}"


# TODO: 4. Check if transaction is successful
# TODO: 2. Check resources sufficient to make drink order


def check_resources(coffee_choice):
    """Check if there are sufficient resources for the coffee machine"""
    water_required = MENU[coffee_choice]["ingredients"]["water"]
    milk_required = MENU[coffee_choice]["ingredients"]["milk"]
    coffee_required = MENU[coffee_choice]["ingredients"]["coffee"]

    if resources["water"] < water_required:
        print("Sorry there is not enough water.")
        return False
    elif resources["milk"] < milk_required:
        print("Sorry there is not enough milk.")
        return False
    elif resources["coffee"] < coffee_required:
        print("Sorry there is not enough coffee.")
        return False
    else:
        return True


# TODO: 3. Process coins


def process_coins(coffee_price):
    """Inserts and processes the coins"""
    print("Please insert coins.")
    quarters = int(input("How many quarts?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickles = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01

    payment = quarters + dimes + nickles + pennies
    change = round(payment - coffee_price, 2)

    return change


# TODO: 5. Make coffee and deduct resources
def deduct_resources(coffee_choice):
    """Deduct resources to make the coffee"""
    water_required = MENU[coffee_choice]["ingredients"]["water"]
    milk_required = MENU[coffee_choice]["ingredients"]["milk"]
    coffee_required = MENU[coffee_choice]["ingredients"]["coffee"]

    resources["water"] -= water_required
    resources["milk"] -= milk_required
    resources["coffee"] -= coffee_required

# TODO: 6. Run coffee machine


def run_coffee_machine():
    run_machine = True
    money = 0.0

    while run_machine:
        user_input = input("What would you like? (espresso/latte/cappuccino): ")

        if user_input == "report":
            print(report(money))
        elif user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
            # Runs the coffee making if there are enough resources
            if check_resources(user_input):
                # User inserts coins and machine checks if there are enough coins
                change = process_coins(MENU[user_input]["cost"])
                if change >= 0:
                    print(f"Here is ${change} dollars in change.")
                    money += MENU[user_input]["cost"]
                    deduct_resources(user_input)
                    print(f"Here is your {user_input}. Enjoy!")
                elif change < 0:
                    print("Sorry that's not enough money. Money refunded.")
        elif user_input == "off":
            run_machine = False


run_coffee_machine()
print("Hello world")

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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

espresso_ingredients = MENU["espresso"]["ingredients"]
latte_ingredients = MENU["latte"]["ingredients"]
cappuccino_ingredients = MENU["cappuccino"]["ingredients"]


def generate_report(inventory, money_collected):
    water = inventory["water"]
    milk = inventory["milk"]
    coffee = inventory["coffee"]
    return f"""Remaining inventory:
     Water: {water}ml
     Milk: {milk}ml
     Coffee: {coffee}g\n
     Profits collected: ${money_collected}"""


def is_enough_resources(order, inventory):
    if order == "espresso":
        if espresso_ingredients["water"] < inventory["water"] and espresso_ingredients["coffee"] < inventory["coffee"]:
            return True
        else:
            return False
    elif order == "latte":
        if latte_ingredients["water"] < inventory["water"] and latte_ingredients["milk"] < inventory["milk"] and latte_ingredients["coffee"] < inventory["coffee"]:
            return True
        else:
            return False
    elif order == "cappuccino":
        if cappuccino_ingredients["water"] < inventory["water"] and cappuccino_ingredients["milk"] < inventory["milk"] and cappuccino_ingredients["coffee"] < inventory["coffee"]:
            return True
        else:
            return False

def calculate_money_entered():
    quarters = int(input("How many quarters do you enter?")) * 0.25
    dimes = int(input("How many dimes?")) * 0.10
    nickels = int(input("How many nickels?")) * 0.05
    pennies = int(input("How many pennies?")) * 0.01
    return quarters + dimes + nickels + pennies


def subtract_ingredients(order, inventory):
    inventory["water"] -= order["water"]
    inventory["milk"] -= order["milk"]
    inventory["coffee"] -= order["coffee"]
    return


# start of program
print("Welcome to Jarod's Coffee Machine!")

machine_off = False
while not machine_off:
    print("Our menu is: espresso, latte, and cappuccino.")
    order = input("What would you like from our menu?").lower()

    if order == "off":
        machine_off = True
    elif order == "report":
        print(generate_report(resources, profit))
    elif order == "espresso":
        order = espresso_ingredients
    elif order == "latte":
        order = latte_ingredients
    elif order == "cappuccino":
        order = cappuccino_ingredients

    if not is_enough_resources(order, resources):
        print("Our apologies. We do not currently have enough ingredients to make your order.")
        break

# TODO: 5. Process coins


# TODO: 6. Check if transaction was successful. If user put enough money in and give them change back.


# TODO: 7. Make coffee and deduct resources used.

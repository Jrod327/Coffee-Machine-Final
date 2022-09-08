MENU = {
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


def generate_report(inventory, money_collected):
    water = inventory["water"]
    milk = inventory["milk"]
    coffee = inventory["coffee"]
    return f"""Remaining inventory:
     Water: {water}ml
     Milk: {milk}ml
     Coffee: {coffee}g\n
     Profits collected: ${money_collected}"""


def check_inventory(inventory, ingredients):
    espresso_resources = MENU.get("espresso", "ingredients")
    latte_resources = MENU.get("latte", "ingredients")
    cappuccino_resources = MENU.get("cappuccino", "ingredients"[0])


def calculate_money_entered():
    quarters = int(input("How many quarters do you enter?")) * 0.25
    dimes = int(input("How many dimes?")) * 0.10
    nickels = int(input("How many nickels?")) * 0.05
    pennies = int(input("How many pennies?")) * 0.01
    return quarters + dimes + nickels + pennies


# start of program
print("Welcome to Jarod's Coffee Machine!")
print(MENU.get("cappuccino", "ingredients"))
machine_off = False
while not machine_off:
    print("Our menu is: espresso, latte, and cappuccino.")
    order = input("What would you like from our menu?").lower()

    if order == "off":
        machine_off = True
    elif order == "report":
        print(generate_report(resources, profit))

# TODO: 4. Check resources sufficient to make drink order.

check_inventory(resources, )

# TODO: 5. Process coins


# TODO: 6. Check if transaction was successful. If user put enough money in and give them change back.


# TODO: 7. Make coffee and deduct resources used.

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


def format_report(inventory, money_collected):
    water = inventory["water"]
    milk = inventory["milk"]
    coffee = inventory["coffee"]
    return f"""Remaining inventory:
     Water: {water}ml
     Milk: {milk}ml
     Coffee: {coffee}g\n
     Profits collected: ${money_collected}"""


def check_inventory(inventory):

print("Welcome to Jarod's Coffee Machine!")

# TODO: 2. Turn coffee machine off to end program.
machine_off = False
while not machine_off:
    print("Our menu is: espresso, latte, and cappuccino.")
    order = input("What would you like from our menu?").lower()

    if order == "off":
        machine_off = True
    elif order == "report":
        print(format_report(resources, profit))

# TODO: 4. Check resources sufficient to make drink order.

check_inventory(resources)

# TODO: 5. Process coins


# TODO: 6. Check if transaction was successful. If user put enough money in and give them change back.


# TODO: 7. Make coffee and deduct resources used.

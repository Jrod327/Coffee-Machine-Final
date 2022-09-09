from menu import MENU, resources, profit


def generate_report(inventory, money_collected):
    water = inventory["water"]
    milk = inventory["milk"]
    coffee = inventory["coffee"]
    return f"""Remaining inventory:
     Water: {water}ml
     Milk: {milk}ml
     Coffee: {coffee}g\n
     Profits collected: ${money_collected}"""


def is_enough_ingredients(order, inventory):
    return order["water"] <= inventory["water"] and order["milk"] <= inventory["milk"] and order["coffee"] <= inventory[
        "coffee"]


def calculate_money_entered():
    quarters = int(input("How many quarters do you enter? ")) * 0.25
    dimes = int(input("How many dimes? ")) * 0.10
    nickels = int(input("How many nickels? ")) * 0.05
    pennies = int(input("How many pennies? \n")) * 0.01
    return quarters + dimes + nickels + pennies


def is_enough_money(money_received, drink_price):
    if money_received >= drink_price:
        if money_received > drink_price:
            change = round(money_received - drink_price, 2)
            print(f"Here is your change: ${change}\n")
        return True
    else:
        print(f"Sorry you didn't enter enough money. Here is your refund of ${money_received}\n")
        return False


def subtract_ingredients_used(order, inventory):
    inventory["water"] -= order["water"]
    inventory["milk"] -= order["milk"]
    inventory["coffee"] -= order["coffee"]


# start of program
print("Welcome to 'Jarod's' Coffee Machine!")

machine_off = False
while not machine_off:
    print("Our menu is: espresso, latte, and cappuccino.\n")
    order = input("What would you like from our menu? ").lower()
    drink = order  # only used this to easily name the drink in an f string later

    if order == "off":
        machine_off = True
        print("Coffee machine shutting down. Goodbye.")
    elif order == "report":
        print(generate_report(resources, profit))
    else:
        order = MENU[order]

        if not is_enough_ingredients(order["ingredients"], resources):
            print("Our apologies; We do not currently have enough ingredients to make your order. Please try a "
                  "different item. \n")
        else:
            print("Please enter coins to pay for your drink.")
            money_received = calculate_money_entered()

            if is_enough_money(money_received, order["cost"]):
                profit += order["cost"]
                print(f"Here is your {drink}. Please enjoy!\n")
                subtract_ingredients_used(order["ingredients"], resources)
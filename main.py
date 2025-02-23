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

def make_selection(resources):
    is_selection_valid = False
    while not is_selection_valid:
        print("What would you like?")
        print("Espresso: $1.50")
        print("Latte: $2.50")
        print("Cappuccino: $3.00")
        selection = input("Please type 'espresso', 'latte', or 'cappuccino': ").lower()
        if selection == "espresso" or selection == "latte" or selection == "cappuccino":
            has_resources_available = check_resources(selection, resources)
            if has_resources_available:
                return selection
        elif selection == "report":
            print_report(resources)
        elif selection == "off":
            exit()
        else:
            print("Please make a valid selection.")

def process_coins():
    print("Please insert coins.")

    coins_inserted = {
        "quarters": {
            "individual_coin_type_value": 0.25,
            "amount": 0,
            "total_coin_type_value": 0,
        },
        "dimes": {
            "individual_coin_type_value": 0.10,
            "amount": 0,
            "total_coin_type_value": 0,
        },
        "nickles": {
            "individual_coin_type_value": 0.05,
            "amount": 0,
            "total_coin_type_value": 0,
        },
        "pennies": {
            "individual_coin_type_value": 0.01,
            "amount": 0,
            "total_coin_type_value": 0,
        }
    }

    total_value_of_all_coins = 0

    for coin_type in coins_inserted:
        is_valid_amount = False
        while not is_valid_amount:
            try:
                coins_inserted[coin_type]["amount"] = int(input(f"How many {coin_type}?: "))
                coins_inserted[coin_type]["total_coin_type_value"] = coins_inserted[coin_type]["individual_coin_type_value"] * coins_inserted[coin_type]["amount"]
                total_value_of_all_coins += coins_inserted[coin_type]["total_coin_type_value"]
                is_valid_amount = True
            except ValueError:
                print("Please enter whole numbers only.")

    return total_value_of_all_coins

def check_if_transaction_successful(selection, total_value_of_all_coins):
    cost_of_drink = MENU[selection]["cost"]
    if total_value_of_all_coins < cost_of_drink:
        print("That's not enough money.  Transaction refunded.")
        return False
    elif total_value_of_all_coins >= cost_of_drink:
        calculate_change(cost_of_drink, total_value_of_all_coins)
        return True

def calculate_change(cost_of_drink, total_value_of_all_coins):
    change_amount = total_value_of_all_coins - cost_of_drink
    if change_amount > 0:
        print(f"Here is ${change_amount:.2f} in change.")

def check_resources(selection, resources):
    for ingredient in MENU[selection]["ingredients"]:
        needed_amount = MENU[selection]["ingredients"].get(ingredient)
        available_amount = resources["ingredients"].get(ingredient)
        if needed_amount > available_amount:
            print(f"Sorry, there is not enough {ingredient} for that drink.")
            return False
    return True

def update_resources(selection, resources):
    for ingredient in MENU[selection]["ingredients"]:
        resources["ingredients"][ingredient] -= MENU[selection]["ingredients"].get(ingredient)
    resources["money"] += MENU[selection]["cost"]

def print_report(resources):
    print(resources)

def start():
    resources = {
        "ingredients": {
            "water": 300,
            "milk": 200,
            "coffee": 100
        },
        "money": 0
    }

    is_machine_on = True

    while is_machine_on:
        selection = make_selection(resources)
        total_value_of_all_coins = process_coins()
        is_valid_transaction = check_if_transaction_successful(selection, total_value_of_all_coins)
        if not is_valid_transaction:
            continue
        update_resources(selection, resources)
        print(f"Here is your {selection}.  Enjoy!")

start()
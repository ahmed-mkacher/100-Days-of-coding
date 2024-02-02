MENU = \
{
    "espresso":
    {
        "ingredients":
        {
            "water": 50,
            "coffee": 18,
            "milk": 0
        },
        "cost": 1.5,
    },
    "latte":
    {
        "ingredients":
        {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino":
    {
        "ingredients":
        {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = \
    {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }


def resources_sufficiency(ingredients):
    for item in ingredients:
        if ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        else:
            return True


profit = 0


def check_payment():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))*0.25
    dimes = int(input("How many dimes?: "))*0.10
    nickles = int(input("How many nickles?: "))*0.05
    pennies = int(input("How many pennies?: "))*0.01
    money = pennies + nickles + dimes + quarters
    return money


def report():
    print(f"Water: {resources['water']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Milk: {resources['milk']}")
    print(f"Money: ${profit}")


while True:
    user_choice = input("What would you like? (latte/espresso/cappuccino): ").lower()
    if user_choice == "off":
        break
    elif user_choice == "report":
        report()
    else:
        drink = MENU[user_choice]
        if resources_sufficiency(drink["ingredients"]):
            payment = check_payment()
            if payment >= drink["cost"]:
                print(f'Here is {"{:.2f}".format(payment - drink["cost"])} in change.')
                profit += payment
                water_quantity = MENU[user_choice]["ingredients"]["water"]
                coffee_quantity = MENU[user_choice]["ingredients"]["coffee"]
                milk_quantity = MENU[user_choice]["ingredients"]["milk"]
                print(f"Here is your {user_choice}. Enjoy!")
                resources["water"] -= water_quantity
                resources["coffee"] -= coffee_quantity
                resources["milk"] -= milk_quantity
            else:
                print("Sorry that's not enough money. Money refunded.")
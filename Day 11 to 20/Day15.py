from data import menuu, resources
from os import system

water = 0
milk = 0
coffee = 0
money = 0
system("clear")
while True:
    ask = input("What would you like? (espresso/latte/cappuccino) : ").lower()
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    if ask == "report":
        print(f"Water: {water}ml \n Milk: {milk}ml \n Coffee: {coffee}g \n Money: ${money}")
        continue

    if ask == "cappuccino" and milk < 100 and water < 250:
        print("Sorry there is not enough water.")
        continue
    elif ask == "latte" and milk < 150 and water < 200:
        print("Sorry there is not enough water.")
        continue
    elif ask == "espresso" and water < 50:
        print("Sorry there is not enough water.")
        break

    if ask == "espresso" or "latte" or "cappuccino":
        item = menuu[ask]
        resources["water"] = resources["water"] - item["ingredients"]["water"]
        resources["milk"] = resources["milk"] - item["ingredients"]["milk"]
        resources["coffee"] =  resources["coffee"] - item["ingredients"]["coffee"]
    else:
        print("Invalid Input")

    quater = float(input("How many quarters?: ")) * 0.25
    dimes = float(input("How many dimes?: ")) * 0.10
    nickles = float(input("How many nickle?: ")) * 0.05
    pennies = float(input("How many pennies?: ")) * 0.01

    cost = item["cost"]
    mon = ((0.25 * quater) + (0.10 * dimes) + (0.05 * nickles) + (0.01 * pennies) )
    if mon >= cost:
        money = money + cost
        print(f"Here is ${round(mon - cost, 2)} in change.\n Here is your {ask} ☕️. Enjoy! ")
    else:
        print("Sorry that's not enough money. Money refunded.")

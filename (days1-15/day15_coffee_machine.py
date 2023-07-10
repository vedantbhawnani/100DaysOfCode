drinks = {"espresso": {
    "water": 50, "coffee": 18, "milk": 0, "cost": 1.50
},
    "latte": {
        "water": 200, "coffee": 24, "milk": 150, "cost": 2.50
},
    "cappuccino": {
        "water": 200, "coffee": 24, "milk": 150, "cost": 3.00
}
}

resources = {
    "water": 300, "coffee": 100, "milk": 200
}

total = 0


def money():
    print("Please insert coins. (Penny/Nickel/Dime/Quarter): \n")
    penny = int(input("Penny: "))
    nickel = int(input("Nickel: "))
    dime = int(input("Dime:"))
    quarter = int(input("Quarter: "))
    money = 0.01*penny + 0.05*nickel + 0.10*dime + 0.25*quarter
    return money


def resource_handler(user):
    resources["water"] = resources["water"] - drinks[user]["water"]
    resources["coffee"] = resources["coffee"] - drinks[user]["coffee"]
    resources["milk"] = resources["milk"] - drinks[user]["milk"]


def is_sufficient(resources, user):
    for key in resources:
        if resources[key] < 0:
            print(f"\nInsufficient {key}. \n")
            return key
    return True


def main():
    cont = True
    while (cont):
        global total
        user = input(
            "What do you feel like having?\n'cappuccino'(3.00)\n'latte'(2.50)\n'espresso'(1.50)\nPress 99 to exit.:\n")
        if user == '99':
            cont = False
        elif user == "report":
            for key in resources:
                print(key, resources[key], "\n")
            print("total ", total, end="\n")
        else:
            chan = money()
            total += chan
            change = chan - drinks[user]["cost"]
            if change < 0:
                print("Not enough money inserted. Please try again!")
            else:
                print("Here is your change. {:.1f}".format(change))

                resource_handler(user)
                # check = is_sufficient
                # if check == True:
                #     print(f"\nPlease enjoy your {user}🍵.\n")
                # else:
                #     print(f"\nInsufficient {check}. \n")
                if is_sufficient(resources, user) == True:
                    print(f"\nPlease enjoy your {user}🍵.\n")
                # for key in resources:
                #     if resources[key] < 0:
                #         print(f"\nInsufficient {key}. \n")
                #         break
                #     else:
                #         print(f"\nPlease enjoy your {user}🍵.\n")


main()

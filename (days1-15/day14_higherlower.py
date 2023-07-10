from day14_files import data
import random
import os

points = 0


def format(account):
    acc_name = account["name"]
    acc_desc = account["description"]
    acc_country = account["country"]
    return f"{acc_name}, a {acc_desc} from {acc_country}."


def check(account_a, account_b):
    return 'A' if account_a["follower_count"] > account_b["follower_count"] else 'B'


def main():
    global points, account_a, account_b
    account_a = random.choice(data)
    if points == 0:
        account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)
    while (1):
        print('''
  _   _ ___ ____ _   _      __  _     _____        __
 | | | |_ _/ ___| | | |    / / | |   / _ \ \      / /
 | |_| || | |  _| |_| |   / /  | |  | | | \ \ /\ / / 
 |  _  || | |_| |  _  |  / /   | |__| |_| |\ V  V /  
 |_| |_|___\____|_| |_| /_/    |_____\___/  \_/\_/   
                                                     
        ''')
        gen = random.randrange(0, 1)
        if gen == 0:
            account_b = account_a
            account_a = random.choice(data)
        if gen == 1:
            account_a = account_b
            account_b = random.choice(data)

        if account_a == account_b:
            account_b = random.choice(data)
        print(f"Your points are {points}")
        print(f"A: {format(account_a)}")
        print('''
:::     :::            :::       ::::::::  
:+:     :+:           :+:       :+:    :+: 
+:+     +:+          +:+        +:+        
+#+     +:+         +#+         +#++:++#++ 
 +#+   +#+         +#+                 +#+ 
  #+#+#+#         #+#           #+#    #+# 
    ###          ###             ########     \n''')

        print(f"B: {format(account_b)}")

        user = input("Which has more followers? 'A' or 'B'? ")
        answer = check(account_a, account_b)
        if user == answer:
            print("Correct!")
            points += 1
            os.system("cls")
        else:
            print("Bzzz...That's the wrong answer..")
            print(f"Your points are {points}")
            exit()


main()

import random
import sys
import pyfiglet as pf
from termcolor import cprint
from colorama import init
init(strip=not sys.stdout.isatty())


def repeat():
    again = input("play again? y/n: ")
    main() if again == 'y' else sys.exit()


def check(user_sum, computer_sum):
    if user_sum > 21:
        print("Dealer wins.")

    elif computer_sum > 21:
        print("You win.")

    elif ((computer_sum < 21) and (computer_sum > user_sum)):
        print("Dealer wins!")

    elif ((computer_sum < user_sum) and (user_sum < 21)):
        print("You win.")

    elif (computer_sum == user_sum):
        print("Draw.")

    repeat()


def user_hit(user_sum, x, user):
    value = random.choice(x)
    user.append(value)
    user_sum += value
    return user_sum


def computer_hit(computer_sum, x, computer):
    value = random.choice(x)
    computer.append(value)
    computer_sum += value
    return computer_sum


def main():

    cprint(pf.figlet_format("Blackjack", font="starwars"),
           'blue', attrs=['bold'])
    x = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user = []
    computer = []
    hit = 'y'
    user_sum = 0
    computer_sum = 0
    user_sum = user_hit(user_sum, x, user)
    user_sum = user_hit(user_sum, x, user)
    computer_sum = computer_hit(computer_sum, x, computer)
    print(f"Your cards: {user}. User score: {user_sum}")
    print("Computer's first card:", computer)
    computer_sum = computer_hit(computer_sum, x, computer)
    while hit == 'y':
        hit = input("Type 'y' to get another card, type 'n' to pass: ")
        if (computer_sum < 17):
            computer_sum = computer_hit(computer_sum, x, computer)
            # check(user_sum, computer_sum)
        if hit == 'y':
            user_sum = user_hit(user_sum, x, user)
            # check(user_sum, computer_sum)
        print(f"Your cards:{user}. Your sum:{user_sum}")
        print(f"Computer's cards:{computer}. Computer sum:{computer_sum}")
        if (hit == 'n'):
            computer_sum = computer_hit(computer_sum, x, computer)
            check(user_sum, computer_sum)

        if (user_sum > 22 or computer_sum > 22):
            check(user_sum, computer_sum)

    repeat()


main()

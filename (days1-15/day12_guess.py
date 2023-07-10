import random
while (1):
    print('''   ____                         _   _                                    _               
  / ___|_   _  ___  ___ ___    | |_| |__   ___     _ __  _   _ _ __ ___ | |__   ___ _ __ 
 | |  _| | | |/ _ \/ __/ __|   | __| '_ \ / _ \   | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__|
 | |_| | |_| |  __/\__ \__ \   | |_| | | |  __/   | | | | |_| | | | | | | |_) |  __/ |   
  \____|\__,_|\___||___/___/    \__|_| |_|\___|   |_| |_|\__,_|_| |_| |_|_.__/ \___|_|   
''')
    print("Welcome to the number guessing game")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. 'Easy' or 'Hard': ")

    if difficulty == 'Easy':
        chance = 10
        break
    elif difficulty == 'Hard':
        chance = 5
        break
    else:
        print("Please type 'Easy' or 'Hard'")


def check(numb, guess):
    if numb > guess:
        print("Too low.")
    elif numb < guess:
        print("Too high.")


def minus():
    global chance
    chance -= 1


def main():
    print(f"You have {chance} chances to guess the number.")
    numb = random.randrange(1, 100)
    guess = int(input("Make a guess: "))
    while (guess != numb):
        if guess != numb:
            minus()
            if chance < 1:
                print("You lost all your lives. Let's start from the top?")
                break
            check(numb, guess)
            print(f"You have {chance} remaining.")
            print("Guess again.\n")
        if guess == numb:
            print("You got it! That's the answer!")

        guess = int(input("Make a guess: "))


main()

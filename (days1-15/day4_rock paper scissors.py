import random
import time

random.seed(None)

def choices(): 
    playerc = input("rock, paper, scissors? ")
    options = ["paper", "scissors", "rock"]
    computerc = random.choice(options)
    choices = {"player": playerc, "computer" : computerc}
    return [playerc, computerc]

def win(player, computer):
    print(f"You chose: {player} \ncomputer chose: {computer}")
    if player == computer: 
        return "its a tie!"
    elif player == "rock":
        if computer == "paper":
            print("Paper catches rock. You lose :(")
        elif computer == "scissors":
            print("Rock twarts Paper. You win! :)")
    elif player == "paper":
        if computer == "rock":
            print("Paper catches rock. You win :)")
        elif computer == "scissors":
            print("scissors cuts Paper. You lose! :(")
    elif player == "scissors":
        if computer == "paper":
            print("Scissors cuts Paper. You win :)")
        elif computer == "rock":
            print("Scissors gets twarted by Rock. You lose! :(")

def main():
    player, computer = choices()
    win(player, computer)

main()

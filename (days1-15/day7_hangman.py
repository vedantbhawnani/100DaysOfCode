import random
import os

print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/      
''')


total = ['godfather', 'inception', 'goodfellas', 'anabelle', 'casablanca']
chosenWord = []
chosenWord = random.choice(total)

print(chosenWord, len(chosenWord))

chance = 5
correct = 0
answer = []


for i in range(0, len(chosenWord)):
    answer.append("_")

endOfGame = False

while not endOfGame:
    print(answer)
    guess = input("Enter an alphabet: ").lower()
    count = 0
    for letter in range(len(chosenWord)):
        if (chosenWord[letter] == guess):
            count = 1
            answer[letter] = chosenWord[letter]
            correct += 1
        if guess == answer[letter]:
            count = 9

    if count == 1:
        print("Correct answer!")
    elif count == 0:
        print("Wrong guess. Hearts - 1")
        chance -= 1
    elif count == 9:
        print("You already guessed it!")
    print(answer)

    if "_" not in answer:
        endOfGame = True
        print("You win")

    if chance == 0:
        print("You die...")

    os.system('cls')

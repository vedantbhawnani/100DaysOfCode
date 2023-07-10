print('''
                                        /\\
                                        )(
                                       /{}\\
                                      (    )
                         ,----------_____....----.--------,
                _____.....-----~~~~~             |_______/ `
               |                                 |      /  |
               |          H E L L O              |     /
               |                                  |   /   /
                |                                 | _/   /
                |      C H A L L E N G E R        |,'|~~
               ,|                                ,'  |
             ,'_|_____________________________:,' /) |.
             |  \    \                /    /  |  (/  |_. .
             |   \    \     {}       /    /   |    .' .  .
          . '|    \    \            / _  /    |    ,   .  .
         . . |\    \    \          _.( ~-.   /|\ ,' .   . .
       ` .  -`_-.--.______..._____( ,/  ` \~-.|,' .   .
        .  `    .     .       .  ,'\. ~-  . , .  .  .   .
           .  `   .     ,   .      , ~~-.' .  .    .


''')

print("Welcome to the game of Choices!")
print("Your mission is to find the treasure")
choice1 = input("LEFT or RIGHT? Quick\n").lower()

if choice1 == 'left':
    print("You were slain and eaten...")
    exit()
else:
    print("Good instincts. I think we could use them...")

choice2 = input("Can you SWIM or should we WAIT for the boat?\n").lower

if choice2 == 'swim':
    print("Did you not see the temperature OR the alligators? Good lord...", end="")
    print("So long Mate")
    exit()
else:
    print("HaHa, look at those alligators looking at us sit cool-ly in the boat. Waiting was the right call.")

choice3 = input("Which door? Red, Blue or Green?\n").lower()

if choice3 == 'Green':
    print("You get to the treasure! Yippiee!!!")
else:
    print("The door was too heavy for you to lift and you were crushed by its weight... Your blood is the only thing near the treasure now...")
    exit()

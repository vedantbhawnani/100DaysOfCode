from  turtle import Turtle, Screen
import random


bet_on = False
screen = Screen()
screen.screensize(500,400)
# screen.bgpic("back.png")
bet = screen.textinput(title = "Make your bet.", prompt = "Which turtle will win the race? Enter your color: ").lower()
y = [-150,-90,-30,30,90,150]

turtules = []
colour=["red","blue", "green", "yellow","violet","orange"]

for _ in range(0,6):
    t = Turtle(shape = "turtle")
    t.color(colour[_])
    t.penup()
    t.goto(-280,y[_])
    # t.pendown()
    turtules.append(t)

# print(turtules) 
if bet:
    bet_on = True

while bet_on:

    for turtule in turtules:
        wee = random.randint(0,10)
        turtule.forward(wee)
        if turtule.xcor()>250:
            bet_on = False
            win = turtule.pencolor()
            if win == bet:
                screen.textinput(title= "You win! {win} wins...")
            else:
                screen.textinput(title = "nope, just not your day... {win} wins..")

screen.exitonclick()
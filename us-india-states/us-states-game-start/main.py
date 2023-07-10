from turtle import *
import pandas as pd

screen = Screen()
screen.title("Guess the states")

screen.addshape("blank_states_img.gif")
shape("blank_states_img.gif")


count = 0
correct = []
remain = []

data = pd.read_csv("50_states.csv")
row = data.state.to_list()

while len(correct) < len(row):
    user = screen.textinput(f"{count}/50 States guessed", "Enter name of state").title()
    if user == "Exit":
        break
    if user in row:
        correct.append(user)
        t = Turtle()
        t.hideturtle()
        name = data[data.state == user]
        t.penup()
        t.goto(int(name.x), int(name.y))
        t.write(user)
        count += 1
        print(count)

for name in row:
    if name not in correct:
        remain.append(name)

pd.Series(data= remain).to_csv("remains.csv")

mainloop()
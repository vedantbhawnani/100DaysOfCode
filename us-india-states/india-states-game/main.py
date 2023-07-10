from turtle import *
import pandas as pd

screen = Screen()
screen.title("Guess the states")

image = "India-state.gif"

screen.addshape(image)
shape(image)


count = 0
correct = []
remain = []

data = pd.read_csv("indian_states.csv")
row = data.state.to_list()

while len(correct) < len(row):
    insert = screen.textinput(f"{count}/50 States guessed", "Enter name of state")
    user = insert.title()
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

pd.DataFrame(data= remain).to_csv("remains.csv")

mainloop()
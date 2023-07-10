from turtle import *
import time
from tkinter import messagebox

from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width = 700, height = 500)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

food = Food()
score = Scoreboard()

flag = True
count = 0

while flag:
    screen.update()
    time.sleep(0.15)
     
    if snake.body[0].distance(food) < 15:
        food.create_food()
        count = score.increase()
        snake.grow()

    check1 = snake.hit()
    check2= snake.move()
    # print(f"{check1}\n{check2}")
    # print(f"{check}")

    if check1 == False or check2 == False:
        # print("check2")
        flag = False

if flag == False:
    # messagebox.showinfo("Game over", f"Game over. You scored {count}")
    score.goto(0,0)
    score.write("GAME OVER", False, align = "center")
screen.exitonclick()
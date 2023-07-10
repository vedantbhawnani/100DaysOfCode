from turtle import Screen, Turtle
import random

class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("green")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed(0)
        self.create_food()

    def create_food(self):
        x = random.randint(-340, 340)
        y = random.randint(-200,230)
        self.goto(x,y) 

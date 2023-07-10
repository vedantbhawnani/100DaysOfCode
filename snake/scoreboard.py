from turtle import *


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.count = 0
        self.color("white")
        self.penup()
        self.goto(0,230)
        self.pendown()
        self.write(f"Score: {self.count}", False, align = "center")
        self.hideturtle()

    def increase(self):
        self.count += 1
        self.clear()
        self.write(f"Score: {self.count}", False, align = "center")
        return self.count

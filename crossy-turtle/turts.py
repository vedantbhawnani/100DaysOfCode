from turtle import Turtle, Screen

level = 0

class Turts(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape('turtle')
        self.setheading(90)
        self.penup()
        self.loc()

    def move(self):
        self.goto(self.xcor(), self.ycor() + 10)

    def loc(self):
        self.goto(0,-270)
    

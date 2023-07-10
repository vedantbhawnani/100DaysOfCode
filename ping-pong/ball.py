from turtle import Turtle

class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.color("White")
        self.penup()       
        self.x = 10
        self.y = 10     

    def move(self):
        self.goto(self.xcor() + self.x, self.ycor() + self.y)


    def collision(self, check):
        if check == 1:
            self.y *= -1
        if check == 2:
            self.x *= -1



    

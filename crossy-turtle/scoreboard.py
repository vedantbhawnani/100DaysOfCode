from turtle import Turtle

class Levels(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.lev = 0
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(-270, 250)
        self.write(f"{self.lev}", align = "center", font = ['Times Roman', 20, 'normal'])

    def increase(self):
        self.lev += 1
        self.clear()
        self.write(f"{self.lev}", align = "center")
        return self.lev

    def win(self):
        self.clear()
        self.goto(0,0)
        self.write("GAME OVER!! You a pro", align="Center")

    def lose(self):
        self.clear()
        self.goto(0,0)
        self.write("GAME OVER!! You played ... well... okayish.", align="Center")
    
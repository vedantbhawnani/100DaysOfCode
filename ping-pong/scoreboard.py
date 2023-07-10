from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.hideturtle()
        self.color("White")
        self.penup()
        self.goto(0,250)
        self.clear()
        self.write(f"{self.l_score}\t\t{self.r_score}", False, 'Center', font=["Verdana",15,"normal"])

    def increase_l(self):
        self.l_score += 1
        self.clear()
        self.write(f"{self.l_score}\t\t{self.r_score}", False, 'Center', font=["Verdana",15,"normal"])

    def increase_r(self):
        self.r_score += 1
        self.clear()
        self.write(f"{self.l_score}\t\t{self.r_score}", False, 'Center', font=["Verdana",15,"normal"])

        
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width = 700, height = 500)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

class Snake():
    def __init__(self) -> None:
        x = 0
        self.body = []
        for _ in range(3):
            t = Turtle(shape = "square")
            
            t.color("White")
            t.penup()
            t.goto(x,0)
            self.body.append(t)
            x -= 20

    def move(self):
        for bodnum in range(len(self.body) - 1,0,-1):
            new_x = self.body[bodnum - 1] .xcor()
            new_y = self.body[bodnum - 1] .ycor()
            self.body[bodnum].goto(new_x, new_y)
        
        self.body[0].fd(20)

        if (abs(self.body[0].xcor()) > 340) or (self.body[0].ycor()>240) or (self.body[0].ycor()<-245) :
            # print("check")
            return False

    def grow(self):
        t = Turtle(shape = "square")
        t.color("White")
        t.penup()
        t.goto(self.body[-1].pos())
        self.body.append(t)

    def hit(self):
        for bod in self.body[1:]:
            if self.body[0].distance(bod) < 10:
                return False

    def up(self):
        if self.body[0].heading() != 270: 
            self.body[0].setheading(90)
    
    def down(self):
        if self.body[0].heading() != 90:
            self.body[0].setheading(270)
    
    def left(self):
        if self.body[0].heading() != 0:
            self.body[0].setheading(180)
    
    def right(self):
        if self.body[0].heading() != 180:
            self.body[0].setheading(0)


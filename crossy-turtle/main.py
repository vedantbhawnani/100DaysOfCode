from turtle import Turtle, Screen
import time

from turts import Turts
from cars import Cars
from scoreboard import Levels

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)
t = Turts()
car = Cars()
score = Levels()

flag = True
check = 1

screen.listen()
screen.onkey(t.move, 'Up')
speed = 0


while flag:
    screen.update()
    time.sleep(0.1)
    car.create_car(speed)
    if t.ycor() > 270:
        speed = score.increase()
        t.loc()
    
    # flag = car.collision(t.ycor())
    for one in car.traffic:
            if one.distance(t) < 18:
                flag = False
                check = 0

    car.move()
    

if check == 1:
    score.goto(0,0)
    score.write("GAME OVER!! You a pro", align="Center")
    
else:
    score.goto(0,0)
    score.write("GAME OVER!! You played ... well... okayish.", align="Center")
    

screen.exitonclick()
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(height=600, width= 800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

flag = True
l_score = 0
r_score = 0

while flag:
    screen.update()
    # score.display()
    time.sleep(0.09)
    ball.move()
    
    if ball.ycor() > 280 or ball.ycor() < -280: 
        ball.collision(1)

    if ball.xcor() >380:
        ball.collision(2)
        score.increase_l()
        
    elif ball.xcor() < -380:        
        ball.collision(2)
        score.increase_r()
        

    if ball.distance(r_paddle) < 40 and ball.xcor() > 320 or ball.distance(l_paddle) < 40 and ball.xcor() < -320:
        ball.collision(2)

screen.exitonclick()
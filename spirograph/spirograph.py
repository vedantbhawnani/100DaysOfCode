import turtle
import random

t = turtle.Turtle()
turtle.colormode(255)
t.pensize(2)
t.speed(0)

def colour():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return r,g,b

for i in range(int(360/5)):
    t.color(colour())
    t.circle(90)
    x = t.heading()
    t.setheading(x + 5)

display = turtle.Screen()
display.exitonclick
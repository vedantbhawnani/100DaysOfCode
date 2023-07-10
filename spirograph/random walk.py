import turtle
import random


t = turtle.Turtle()
# t.pencolor("white")
# t.setpos(-100, 100)
# t.pencolor("black")

turtle.colormode(255)

def colour():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return r,g,b

directions = [360,180,270,90]
color = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

t.pensize(7)
t.speed(7)

for i in range (1000):
    r,g,b = colour()
    t.pencolor(r,g,b)
    t.setheading(random.choice(directions))
    t.forward(20)

myscreen = turtle.Screen()
myscreen.exitonclick()
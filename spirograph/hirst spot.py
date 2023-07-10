import colorgram
import turtle
import random


# rgb_colors = []
# color = colorgram.extract('C:\\Users\\vedan\\codes\\100DaysOfCofe\\day18\\spot.jpg', 50)
# for colour in color:
#     r = colour.rgb.r
#     g = colour.rgb.g
#     b = colour.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

colors = [(212, 154, 97), (52, 108, 132), (178, 78, 33), (198, 143, 34), (123, 80, 97), (235, 240, 244), (116, 155, 171), (124, 175, 158), (228, 197, 129), (194, 85, 105), (54, 38, 20), (12, 51, 65), (189, 123, 142), (54, 120, 115), (41, 169, 126), (167, 21, 31), (225, 94, 78), (4, 30, 28), (39, 32, 34), (243, 163, 159), (81, 148, 168), (164, 27, 22), (239, 163, 167), (104, 123, 159), (164, 209, 193), (21, 81, 93), (29, 85, 81), (162, 206, 212), (53, 62, 81), (183, 190, 206), (85, 74, 35)]


def draw():
    for i in range(10):
        t.dot(15,random.choice(colors))
        t.penup()
        t.forward(30)
        t.pendown()


t = turtle.Turtle()
turtle.colormode(255)
t.penup()
t.speed(10)
t.setpos(-100,-100)


m,n = t.position()
t.hideturtle()
for _ in range(10):
    draw()
    t.penup()
    n = n + 30
    # m = m + 20
    t.goto(m, n)
    t.pendown()

screen = turtle.Screen()
screen.exitonclick()
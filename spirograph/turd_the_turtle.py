from turtle import Turtle, Screen

# def right():
#     for i in range(3):
#         t.left(90)

t = Turtle()
t.shape("arrow")

for i in range(6):
    t.pencolor("REd")
    t.fd(100)
    t.right(60)


for i in range(3):
    t.fd(100)
    t.right(120)

for i in range(5):
    t.fd(100)
    t.right(72)


for i in range(7):
    t.fd(100)
    t.right(51.4285714)


for i in range(4):
    t.fd(100)
    t.right(90)


for i in range(8):
    t.fd(100)
    t.right(45)


myscreen = Screen()
myscreen.exitonclick()
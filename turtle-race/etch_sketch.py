import turtle

def right():
    t.fd(10)


def left():
    t.bk(10)


def up():
    t.right(10)

def down():
    t.left(10)


t = turtle.Turtle()
t.shape("turtle")
screen = turtle.Screen()
turtle.colormode(255)

screen.listen()
screen.onkey(key = "w",fun = left)
screen.onkey(key = "s", fun = right)
screen.onkey(key = "d", fun = up)
screen.onkey(key = "a", fun = down)


screen.exitonclick() 

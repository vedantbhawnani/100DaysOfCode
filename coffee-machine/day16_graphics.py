from turtle import *
from prettytable import *
import pandas as pd


def turt():
    turts = Turtle()
    turts.shape("turtle")
    turts.color("red")
    turts.forward(20)
    my_screen = Screen()
    print(my_screen.canvheight)
    my_screen.exitonclick()


def tables_self():
    pt = PrettyTable()
    df = pd.read_csv("E:\\Datasets\\pokemon\\pokemon.csv")
    x = []
    x.append(df['Name'])
    pt.add_row(x)
    print(pt)


def tables():
    pt = PrettyTable()
    pt.add_column("wishlist", ["you", "me", "on", "a", "couch"], align="l")
    print(pt)


tables()

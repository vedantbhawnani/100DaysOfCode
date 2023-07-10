from tkinter import *
import pandas as pd
import random
import time

BACKGROUND = "#3D8361"
CARD = "#1C6758"

root = Tk()
root.config(bg=BACKGROUND, padx=50, pady=50)
root.minsize(800,1000)
root.title("Flash Cards")

completed =[]

def countdown():
    time.sleep(1)

def get_index():
    index = random.randrange(1,101)
    return index

def words():
    file = pd.read_csv("100DaysOfCode/day30/french_words.csv")
    index = get_index()
    while index in completed:
        index = get_index()
    completed.append(index)
    french_word = file.French[index]
    english_word = file.English[index]
    return french_word, english_word

def create_front():

    french, english = words()

    canvas = Canvas(root, width=800, height=526, bg="#3D8361", highlightthickness="0")
    canvas.create_image(400,268, image = front)
    canvas.create_text(400,170,text="French", font = ("Arial", 40, "italic"))
    canvas.create_text(400,290,text=french, font = ("Times Roman", 50, "bold"))

    canvas.grid(row=0, column=2)

    for i in range(5):
        countdown()
        canvas.update()
    create_back(english)


def create_back(english):

    canvas = Canvas(root, width=800, height=526, bg="#3D8361", highlightthickness="0")
    canvas.create_image(400,268, image = back)
    canvas.create_text(400,170,text="English", font = ("Arial", 40, "italic"))
    canvas.create_text(400,290,text=english, font = ("Times Roman", 50, "bold"))

    canvas.grid(row=0, column=2)


def tick():
    print(completed)
    create_front()


def cross():
    completed.pop()
    print(completed)
    create_front()

check = PhotoImage(file = "100DaysOfCode\day30\\right.png")
wrong = PhotoImage(file = "100DaysOfCode\\day30\\wrong.png")
front = PhotoImage(file = "C:/Users/vedan/codes/100DaysOfCode\day30/card_front.png")
back = PhotoImage(file="100DaysOfCode\day30\card_back.png")

tick = Button(image = check,command = tick)
tick.place(x = 530, y = 550)


cross = Button(image = wrong, command = cross)
cross.place(x = 130, y = 550)

create_front()



mainloop()
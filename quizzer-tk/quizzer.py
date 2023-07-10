import requests
import random
from tkinter import *
import time
import html

response = requests.get(url="https://opentdb.com/api.php?amount=50&type=boolean")
response.raise_for_status()
data = response.json()

QUESTION = '#cff1e7'
BACK = '#497174'
RED_BUTTON = '#ff5a54'
GREEN_BUTTON = '#74da7f'


question_list = []
answer = [] 
done = [0]

points = 0
current = 0

for i in range(len(data['results'])):
    question_list.append(data['results'][i]['question'])
    answer.append(data['results'][i]['correct_answer'])

def get_num():
    num = random.randint(1,49)
    current = num
    return current

def question():
    global current
    while current in done:
        current = get_num()
    done.append(current)
    canvas.config(bg = QUESTION)
    canvas.itemconfig(quest, text = html.unescape(question_list[current]))
    root.update()

def correct():
    global points, current
    num = 1
    if answer[current] == "True":
        canvas.config(bg = "green")
        points += 1
        l1.config(text=f"Points : {points}")

    else:
        canvas.config(bg = "red")

    root.update()
    time.sleep(1)
    question()


def wrong():
    global current, points
    if answer[current] == "True":
        canvas.config(bg = "green")
    else:
        canvas.config(bg = "red")    
        points += 1
        l1.config(text=f"Points : {points}")
    root.update()
    time.sleep(1)
    question()

root = Tk()
root.title("QUIZZERR")
root.minsize(width=600, height=600)
root.config(bg = BACK)

tick = PhotoImage(file = "100DaysOfCode\\quizzer-tk\\tick.png")
cross = PhotoImage(file = "100DaysOfCode\\quizzer-tk\\cross.png")

canvas = Canvas(root,width=400, height=300, bg=QUESTION,highlightthickness= 0)
quest = canvas.create_text(200,150,text=question_list[0], width=300, font = ("Times New Roman", 16, 'bold'))
canvas.place(x =100,y = 70)

l1 = Label(root, text = f"Points: {points}", font = ("Times New Roman", 13, 'bold'), bg = BACK)
l1.place(x=480, y = 20)

b1 = Button(root, image=tick, background=GREEN_BUTTON, command=correct)
b1.place(x = 120, y = 400)

b2 = Button(root, image=cross, background=RED_BUTTON, command=wrong)
b2.place(x = 350, y = 400)

root.update()
root.mainloop()

with open("C:\\Users\\vedan\\codes\\100DaysOfCode\\quizzer-tk\\highscore.txt","a") as leaderboard:
    leaderboard.write(f"{str(points)}\n")
        
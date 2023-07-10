from tkinter import *
from tkinter import messagebox
import time

work_min = 25
break_min = 5
long_break = 20

count = 0
temp = 25*60

def start():
    global count, temp
    temp = work_min*60
    while temp > -1:
        mins,secs = divmod(temp, 60)
        canvas.itemconfig(time_text, text = "{0:2d}:{1:2d}".format(mins,secs))

        root.update()
        time.sleep(1)

        if count == 4:
            long_break()
        if temp == 0:
            count += 1
            small_break()
        temp -= 1

def reset():
    global temp, count
    count = 0
    temp = -1
    canvas.itemconfig(time_text, text = "00:00")

def small_break():
    global temp, count
    temp = break_min*60
    while temp > -1:
        mins,secs = divmod(temp, 60)
        canvas.itemconfig(time_text, text = "{0:2d}:{1:2d}".format(mins, secs))
        root.update()
        time.sleep(1)
        temp -= 1
    start()

def l_break():
    global temp, count
    temp = long_break*60
    while temp > -1:
        mins,secs = divmod(temp, 60)
        canvas.itemconfig(time_text, text = "{0:2d}:{1:2d}".format(mins, secs))
        root.update()
        time.sleep(1)
        temp -= 1


def settings():
    def save():
        global work_min, break_min, long_break
        work_min = int(s1.get())
        break_min = int(s2.get())
        long_break = int(s3.get())

    settings = Toplevel(root)
    settings.title("Settings")
    settings.minsize(200,200)
    
    Label(settings, text="Settings", font=('Helvetica 17 bold')).place(x=50,y=10)
    Label(settings, text="Pom time", font=('Helvetica 12 normal')).place(x=20, y =50)
   
    s1 = Entry(settings, width = 12)
    s1.place(x = 110, y = 50)
    
    Label(settings, text="Short Break", font=('Helvetica 12 normal')).place(x=20, y = 80)
    s2 = Entry(settings, width = 12)
    s2.place(x = 110, y = 80)

    Label(settings, text="Long Break", font=('Helvetica 12 normal')).place(x=20, y = 110)
    s3 = Entry(settings, width = 12)
    s3.place(x = 110, y = 110)
    
    Button(settings, text = "Save", command= save).place(x = 50, y = 140)


root = Tk()
root.title("Pomodoro Timer")
root.minsize(300,350)
root.config(bg="#CEEDC7", padx= 40, pady=25)

l1 = Label(root, text = "WORK", font = ("Times New Roman", 15, "bold"), foreground="#86C8BC", background="#CEEDC7",  highlightthickness="0")
l1.grid(row=0, column=0)

canvas = Canvas(root, width=230, height=200, bg="#CEEDC7", highlightthickness="0")
tomato = PhotoImage(file="C:\\Users\\vedan\\codes\\100DaysOfCode\\pomodoro\\tomato.png")
canvas.create_image(120,100, image = tomato)
time_text = canvas.create_text(120,105,text="00:00", font = ("", 18, "bold"), fill="white")
canvas.grid(row=1, column=0)

b1 = Button(root, text = "Start", command = start)
b1.place(x=70, y = 220)

b2 = Button(root, text = "Reset", command=reset)
b2.place(x=145, y = 220)

b3 = Button(root, text = "Small Break", command=small_break)
b3.place(x=40, y = 260)

b4 = Button(root, text = "Long Break", command=l_break)
b4.place(x=140, y = 260)

b5 = Button(root, text = "Settings", command=settings)
b5.place(x=100, y = 290)

root.mainloop()
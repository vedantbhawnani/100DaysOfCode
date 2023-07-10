import requests
from tkinter import *

root = Tk()
root.minsize(width=600, height=700)
root.title("Kanye says...")

def says():
    response = requests.get(url = "https://api.kanye.rest/")
    data = response.json()
    canvas.itemconfig(quote_text, text = data['quote'])
    root.update()
    

canvas = Canvas(root, width=800, height=800)
bg = PhotoImage(file=r"100DaysOfCode\\kanye says\\bg quotes\\background.png")
canvas.create_image(200,200,image = bg)
quote_text = canvas.create_text(200,180,text = "Press me to see what i say", width=250, font = ("Times New Roman", 16, "bold"))
canvas.place(x = 100, y = 80)

kanye = PhotoImage(file = "100DaysOfCode\\kanye says\\bg quotes\\kanye.png")
b1 = Button(root, image=kanye, command=says)
b1.place(x=230, y = 500)

root.mainloop()
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import json

import secrets
import string
import pyperclip #to copy generated password to clipboard automatically


root = Tk()
root.minsize(500,500)
root.title("Password Manager")
root.config(bg="White")

EMAIL = StringVar()
EMAIL.set("vedant.bhawnani@gmail.com")

s = Style()
s.configure('Fun.TButton', font =
               ('calibri', 10, 'bold'),
                foreground = 'Black')

def safe():
    def yes():
        passw = e3.get()
        web = e1.get()
        email = e2.get()

        new_data = {
            web: {
                "email" : email,
                "password" : passw
        }
    }

        try:
            with open(r"C:\Users\vedan\codes\100DaysOfCode\day29\pass_saver.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open(r"C:\Users\vedan\codes\100DaysOfCode\day29\pass_saver.json", "w") as file:
                json.dump(new_data, file, indent=3)
        else:
            data.update(new_data)
            with open(r"C:\Users\vedan\codes\100DaysOfCode\day29\pass_saver.json", "a") as file:
                json.dump(data, file, indent=3)

        e3.delete(0,END)
        e1.delete(0,END) 
        messagebox.showinfo(title="Saved", message="Your details were saved succesfully.")
        save.destroy()     
    
    passw = e3.get()
    web = e1.get()
    save = Toplevel(root, padx=30, pady=30)
    save.title("Confirm")
    save.minsize(300,200)
    Label(save, text = "Email: ", font=("Sans Serif", "13" ,"bold")).grid(row = 0, column = 0)
    Label(save, textvariable = EMAIL).grid(row=0, column=1)
    Label(save, text = "Password: ").grid(row = 1, column = 0)
    Label(save, text = passw).grid(row=1, column=1)
    Label(save, text = "Website: ").grid(row=2, column=0)
    Label(save, text = web).grid(row=2, column=1)
    Label(save, text = "Is this okay?").place(x=90,y=80)
    Button(save, text = "Yes, Save", command=yes).place(x = 40, y = 110)
    Button(save, text = "No, go back", command= save.destroy).place(x = 140, y = 110)
    

def generate():
    alpha = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    total = alpha + digits + special
    password = ''
    for i in range(16):
        password += ''.join(secrets.choice(total))
    pyperclip.copy(password)
    e3.insert(0, password)
    
def search():
    website = e1.get()
    try:
        with open("C:\\Users\\vedan\\codes\\100DaysOfCode\\day29\\pass_saver.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="File Error",message="No file found.")
    except json.decoder.JSONDecodeError:
        messagebox.showerror(title="File Error",message="File is empty.")
    else:
        if website in data:
            e3.delete(0,END)
            e3.insert(0,data[website]["password"])
            e2 .delete(0,END)
            e2.insert(0,data[website]["email"])
        else:
            messagebox.showerror(title="Data not found", message="Data you are trying to look for isn't saved.")


canvas = Canvas(root, width=300, height=300, bg="white", highlightbackground="white")
lock = PhotoImage(file = r"C:\Users\vedan\codes\100DaysOfCode\day29\logo.png")
canvas.create_image(150,150, image = lock)
canvas.pack()

l1 = Label(root, text="Website", background="white")
l1.place(x=50,y=300)

search_button = Button(text = "Search", style = "Fun.TButton", width= 7, command = search)
search_button.place(x = 330, y = 299)

e1 = Entry(root, width=30)
e1.place(x=140, y = 300)

l2 = Label(root, text="E-mail", background="white")
l2.place(x=50, y = 330)

e2 = Entry(root, width=30, textvariable=EMAIL)
e2.place(x=140, y = 330)

l3 = Label(root, text = "Password", background="white")
l3.place(x=50, y = 360)

e3 = Entry(root, width=30)
e3.place(x=140, y = 360)

b1 = Button(text = "Generate password" ,command=generate)
b1.place(x= 340, y = 357)

b2 = Button(text = "SAVE", style="Fun.TButton",width= 30, command = safe)
b2.place(x = 140, y = 390)



    


root.mainloop()
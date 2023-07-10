from tkinter import *

# def convert(kms):
#     return (kms/1.609)

def convert1():
    e2.delete(0,END)
    string = e1.get()
    if string != '':
       ans = float(string)/1.609
       l4.config(text="{:.2f}".format(ans))
    else:
        l4.config(text = "Value box empty for required conversion")
        


    
def convert2():
    e1.delete(0,END)
    string = e2.get()
    if string != '':
       ans = float(string)*1.609
       l4.config(text="{:.2f}".format(ans))
    else:
        l4.config(text = "Value box empty for required cconversion")


root = Tk()
root.minsize(300,300)
root.title("In progress")
l1 = Label(root, text = "Converter", font=("Arial", 16, "normal"))
l1.grid(row=1, column=2)

l2 = Label(root, text = "Kilometers").grid(row=2, column=1)
e1 = Entry(root, width = 10)
e1.grid(row = 2, column= 2)


l2 = Label(root, text = "Miles").grid(row=3, column=1)
e2 = Entry(root, width = 10)
e2.grid(row = 3, column= 2)

# entry= Entry(root, width= 40)
# # entry.set()
# string = entry.get()
b1 = Button(root, text = "Convert kms to miles", command=convert1)
b1.grid(row=2, column=3)

b2 = Button(root, text = "Convert miles to kms", command=convert2)
b2.grid(row=3 , column=3)

l3 = Label(root, text = "Answer")
l3.grid(row = 6, column = 1)

l4 = Label(root, text = '')
l4.grid(row=6, column= 2)


mainloop()
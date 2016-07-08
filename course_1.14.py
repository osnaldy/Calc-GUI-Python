from tkinter import *


#Using the Enter from the key board
root = Tk()

label1 = Label(root, text = "Enter and Expression: ")
label1.pack()

def evaluate(event):
    data = e.get()
    ans.configure(text = "Answer: " + str(eval(data)))

e = Entry(root)

e.bind("<Return>", evaluate)
e.pack()

ans = Label(root)
ans.pack()

root.mainloop()
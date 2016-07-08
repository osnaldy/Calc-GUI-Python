from tkinter import *


root = Tk()

def leftClick(event):
    print("Hello left")

def rightClick(event):
    print ("Hello right")

def scroll(event):
    print("Hello scroll")

def leftKey(event):
    print("Hello LeftKey")

def rightKey(event):
    print ("Hello RighKey")

root.geometry("500x500")

root.bind("<Button-1>", leftClick)
root.bind("<Button-2>", rightClick)
root.bind("<Button-3>", scroll)
root.bind("<Left>", leftKey)
root.bind("<Right>", rightKey)


root.mainloop()

from tkinter import *
import tkinter.messagebox

#messageBox
#ask Questions

root = Tk()

tkinter.messagebox.showinfo('Response', "Did you know that the world exploded")

answer = tkinter.messagebox.askquestion("Question1", "Are you Human")

if answer == 'yes':
    tkinter.messagebox.showinfo('Congrats', "Thanks God")

if answer == 'no':
    tkinter.messagebox.showinfo('Alien', "You are 100% confirmed Alien")


root.mainloop()
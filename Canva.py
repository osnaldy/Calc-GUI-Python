from tkinter import *
import random

root = Tk()

#with canvas with can add symbols, shapes and more
canvas = Canvas(root, width = 300, height = 300)
canvas.pack()

color = ["red", "orange", "yellow", "green", "blue", "violet", "pink", "black"]

def randomRect(num):

    for i in range(0,num):
        x1 = random.randrange(150)
        y1 = random.randrange(150)
        x2 = x1 + random.randrange(150)
        y2 = y1 + random.randrange(150)

        canvas.create_rectangle(x1,x2,y1,y2, fill = random.choice(color))

randomRect(150)

root.mainloop()
from tkinter import *
import time

root = Tk()

canvas = Canvas(root, width = 300, height = 300)
canvas.pack()

canvas.create_polygon(10,10,10,60,50,35)

#WhenEver you click enter button, the figure will move 10 pixels forward in the x axis

def evaluate(event):
    canvas.move(1,10,0)
    root.update()
    time.sleep(0.1)

root.bind("<Return>", evaluate)

root.mainloop()
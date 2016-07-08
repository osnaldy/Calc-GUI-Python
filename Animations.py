from tkinter import *
import time

root = Tk()

canvas = Canvas(root, width = 300, height = 300)
canvas.pack()

canvas.create_polygon(10,10,10,60,50,35)
canvas.create_rectangle(20,20,100,80)


for i in range(0,100):
    e = canvas.move(1,5,0)
    canvas.move(2,5,0)
    root.update()
    time.sleep(0.1)

root.mainloop()
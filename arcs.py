from tkinter import *

root = Tk()

#with canvas with can add symbols, shapes and more
canvas = Canvas(root, width = 300, height = 300)
canvas.pack()
canvas.create_arc(10,10,200,80, extent = 45, style = ARC)
canvas.create_arc(10,80,200,160, extent = 90, style = ARC)

canvas.create_text(150, 150, text = "This is my first GUI test and it's awesome",
                   font = ("Times", 12), fill = "Red")

root.mainloop()
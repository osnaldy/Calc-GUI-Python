#Create Menus

from tkinter import *

root = Tk()

def random():
    print ("This a statement Func")

mainMenu = Menu(root)

root.configure(menu = mainMenu)

subMenu = Menu(mainMenu)

mainMenu.add_cascade(label = 'File', menu = subMenu)

subMenu.add_command(label = "Random Func", command = random)

subMenu.add_command(label = "New File", command = random)

subMenu.add_separator()

subMenu.add_command(label = "Save Me MF", command = random)

root.mainloop()
from tkinter import *

f = Tk()
f.title("Calculator")

root = Frame(f)
root.pack(expand = True)

equa = ""

equation = StringVar()

calculation = Label(root, textvariable = equation)

equation.set("Enter Your Equation")

calculation.grid(columnspan = 4)

def btnPress(num):
    global equa
    equa = equa + str(num)

    equation.set(equa)

def EqualPress():

    global equa
    total = eval(equa)
    equation.set(total)
    equa = ""

def clear():
    global equa
    equa = ""
    equation.set("")

Button0 = Button(root, text = '0', command = lambda :btnPress(0), width = 5, bg = 'red', fg = 'blue')
Button0.grid(row = 4, column = 0)

Button1 = Button(root, text = '9', command = lambda :btnPress(9), width = 5)
Button1.grid(row = 1, column = 0)

Button2 = Button(root, text = '8', command = lambda :btnPress(8), width = 5)
Button2.grid(row = 1, column = 1)

Button3 = Button(root, text = '7', command = lambda :btnPress(7), width = 5)
Button3.grid(row = 1, column = 2)

Button4 = Button(root, text = '6', command = lambda :btnPress(6), width = 5)
Button4.grid(row = 2, column = 0)

Button5 = Button(root, text = '5', command = lambda :btnPress(5), width = 5)
Button5.grid(row = 2, column = 1)

Button6 = Button(root, text = '4', command = lambda :btnPress(4), width = 5)
Button6.grid(row = 2, column = 2)

Button7 = Button(root, text = '3', command = lambda :btnPress(3), width = 5)
Button7.grid(row = 3, column = 0)

Button8 = Button(root, text = '2', command = lambda :btnPress(2), width = 5)
Button8.grid(row = 3, column = 1)

Button9 = Button(root, text = '1', command = lambda :btnPress(1), width = 5)
Button9.grid(row = 3, column = 2)

plus = Button(root, text = '+', command = lambda :btnPress("+"), width = 5)
plus.grid(row = 1, column = 3)

minus = Button(root, text = '-', command = lambda :btnPress("-"), width = 5)
minus.grid(row = 2, column = 3)

multiply = Button(root, text = '*', command = lambda :btnPress("*"), width = 5)
multiply.grid(row = 3, column = 3)

divide = Button(root, text = '/', command = lambda :btnPress("/"), width = 5)
divide.grid(row = 4, column = 3)

equals = Button(root, text = '=', command = EqualPress, width = 5)
equals.grid(row = 4, column = 2)

Clear = Button(root, text = "C", command = clear, width = 5)
Clear.grid(row = 4, column = 1)

root.mainloop()
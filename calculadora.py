from tkinter import * 
from math import *
from tkinter import font


root = Tk()
root.title("Calculadora")
root.geometry("377x315")
root.resizable(False, False)
root.configure(background= "#FFDF2D")

Text_screen = StringVar()

display = Entry(root, font=("Calibri 17"), borderwidth=10, justify= "right",
textvariable= Text_screen)
display.grid(row=0, columnspan=6, padx=5, pady=5, sticky=W +E)

wid= 12
hei= 2

operator = " "

def click(b):
    global operator
    operator += str(b)
    Text_screen.set(operator)

def clear_screen():
    global operator
    operator = ""
    Text_screen.set(operator)    

def result():
    global operator
    try:
        r = str(eval(operator))
    except:
        r = "Error"
    Text_screen.set(r)

Label_1 = Label(root, text="Calculator Sm1le", font=("britannic bold", 11))
Label_1.grid(row=1, columnspan=6, padx=5, pady=5, sticky = W +E)

button_7 = Button(root, text="7", width = wid, height = hei, command = lambda: click(7))

button_8 = Button(root, text="8", width = wid, height = hei, command = lambda: click(8))

button_9 = Button(root, text="9", width = wid, height = hei, command = lambda: click(9))

button_4 = Button(root, text="4", width = wid, height = hei, command = lambda: click(4))

button_5 = Button(root, text="5", width = wid, height = hei, command = lambda: click(5))

button_6 = Button(root, text="6", width = wid, height = hei, command = lambda: click(6))

button_1 = Button(root, text="1", width = wid, height = hei, command = lambda: click(1))

button_2 = Button(root, text="2", width = wid, height = hei, command = lambda: click(2))

button_3 = Button(root, text="3", width = wid, height = hei, command = lambda: click(3))

button_punto = Button(root, text=".", width = wid, height = hei, command = lambda: click ("."))

button_0 = Button(root, text="7", width = wid, height = hei, command = lambda: click(0))

button_result = Button(root, text="result", width = wid, height = hei, command = lambda: result())

button_ac = Button(root, text="AC", width = wid, height = hei, command = lambda: clear_screen())
button_suma =  Button(root, text="+", width = wid, height = hei, command = lambda: click ("+"))
button_resta =  Button(root, text="-", width = wid, height = hei, command = lambda: click ("-"))
button_mult =  Button(root, text="*", width = wid, height = hei, command = lambda: click ("*"))
button_div =  Button(root, text="/", width = wid, height = hei, command = lambda: click ("/"))



button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)

button_punto.grid(row=5, column=0)
button_0.grid(row=5, column=1)
button_ac.grid(row=5, column=2)

button_suma.grid(row=6, column=0)
button_resta.grid(row=6, column=1)
button_mult.grid(row=6, column=2)
button_div.grid(row=6, column=3)



button_result.grid(row=2, column=3, rowspan=4, sticky = N+S)






root.mainloop()


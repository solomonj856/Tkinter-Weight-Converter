#from tkinter import *

import tkinter
import random

#ttk more stylized

window = tkinter.Tk()
window.geometry("290x250") #width x height pixels
#window.configure(bg="cyan")
window.title("Weight Converter")

title = tkinter.Label(window, text = "kg", fg = "White", bg="Grey", width=7, height=1, borderwidth=2, relief ="groove")
title.grid(column=0, row=0)

gram = tkinter.Label(window, text="Grams", font=("Arial", 10), fg = "Blue").grid(column=0, row=2)
pound = tkinter.Label(window, text="Pounds", font=("Arial", 10), fg = "Red").grid(column=1, row=2)
ounce = tkinter.Label(window, text="Ounces", font=("Arial", 10), fg = "Orange").grid(column=2, row=2)
stone = tkinter.Label(window, text="Stones", font=("Arial", 10), fg = "Green").grid(column=1, row=4)
weight = tkinter.Label(window, text="", font=("Arial", 10), fg = "Black")
weight.grid(column=1, row=5)

t0 = tkinter.Text(window, height=1, width = 10)
t0.grid(column=0, row=1)

t1 = tkinter.Text(window, height=1, width = 10)
t1.grid(column=1, row=1)

t2 = tkinter.Text(window, height=1, width = 10)
t2.grid(column=2, row=1)

t3 = tkinter.Text(window, height=1, width = 10)
t3.grid(column=1, row=3)

e1value = tkinter.StringVar()

e1 = tkinter.Entry(window, textvariable=e1value)
e1.grid(column=1, row=0) #position


def convert():
    grams = float(e1value.get()) * 1000
    t0.delete("1.0", tkinter.END)
    t0.insert(tkinter.END, grams)


    pounds = float(e1value.get())* 2.20462

    if pounds <= 105:
        weight.configure(text="Minimumweight")
    elif pounds >= 105 and pounds < 108:
        weight.configure(text="Light flyweight")
    elif pounds >= 108 and pounds < 112:
        weight.configure(text="Flyweight")
    elif pounds >= 112 and pounds < 115:
        weight.configure(text="Super flyweight")
    elif pounds >= 115 and pounds < 118:
        weight.configure(text="Bantamweight")
    elif pounds >= 118 and pounds < 122:
        weight.configure(text="Super bantamweight")
    elif pounds >= 122 and pounds < 126:
        weight.configure(text="Featherweight")
    elif pounds >= 126 and pounds < 130:
        weight.configure(text="Super featherweight")
    elif pounds >= 130 and pounds < 135:
        weight.configure(text="Lightweight")
    elif pounds >= 135 and pounds < 140:
        weight.configure(text=" Super lightweight")
    elif pounds >= 140 and pounds < 147:
        weight.configure(text=" Welterweight")
    elif pounds >= 147 and pounds < 154:
        weight.configure(text=" Super welterweight")
    elif pounds >= 154 and pounds < 160:
        weight.configure(text=" Middleweight")
    elif pounds >= 160 and pounds < 168:
        weight.configure(text=" Super middleweight")
    elif pounds >= 168 and pounds < 175:
        weight.configure(text=" Light heavyweight")
    elif pounds >= 175 and pounds < 200:
        weight.configure(text=" Cruiserweight")
    elif pounds >= 200:
        weight.configure(text="Heavyweight")


    t1.delete("1.0", tkinter.END)
    t1.insert(tkinter.END, pounds)

    ounces = float(e1value.get()) * 35.274
    t2.delete("1.0", tkinter.END)
    t2.insert(tkinter.END, ounces)
    
    stones = float(e1value.get()) * 0.157473
    t3.delete("1.0", tkinter.END)
    t3.insert(tkinter.END, stones)




b1 = tkinter.Button(window, text="Convert", command=convert, bg = 'yellow', fg = 'blue')
b1.grid(column=2, row= 0)

window.mainloop() #executes file


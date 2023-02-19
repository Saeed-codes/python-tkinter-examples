import tkinter
from tkinter import *
top = tkinter.Tk()
top.title("A Simple GUI")
top.geometry("350x200")
lab0 = Label(top, width=10)
lab0.grid(column=0, row=0)
lab1 = Label(top, text="This is our first GUI")
lab1.grid(column=1, row=0)
lab2 = Label(top, text="",width=10)
lab2.grid(column=1, row=1)
def click():
 lab2.configure(text="Hello Python!")
def close():
 exit()
btn = Button(top, text ="Greet", command=click)
btn.grid(column=1, row=3)
btn1 = Button(top, text ="Close", command=close)
btn1.grid(column=1, row=4)
top.mainloop()
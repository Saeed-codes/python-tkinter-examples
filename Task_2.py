from tkinter import *
from tkinter import ttk
def show():
 global e2,e1
 e3=e1.get()
 e4=e2.get()
 l3.config(text="Name:"+e3)
 l4.config(text="Email:"+e4)

def close():
 exit()
root=Tk()
root.title('Form')
root.geometry("350x200")
e1=Entry(root)
e1.grid(row=4,column=5)
e2=Entry(root)
e2.grid(row=6,column=5)
e3=e1.get()
answer=Button(root,text="show",command=show).grid(row=8,column=4,sticky=W)
answer=Button(root,text="quit",command=close).grid(row=8,column=0,sticky=W)
l1=Label(root,text="Name")
l1.grid(row=4,column=0,sticky=W)
l2=Label(root,text="Email")
l2.grid(row=6,column=0,sticky=W)
l3=Label(root,text="")
l3.grid(row=10,column=0,sticky=W)
l4=Label(root,text="")
l4.grid(row=12,column=0,sticky=W)
mainloop()
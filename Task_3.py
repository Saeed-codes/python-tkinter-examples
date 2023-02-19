from tkinter import *
from tkinter import ttk
width=260
height=180
x=0
root=Tk()
root.title("Calculator")
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)
def plus():
 global x,e1
 l4.config(text="")
 e3=e1.get()
 if(e3.isnumeric()):
  x+=int(e3)
  l3.config(text=""+str(x))
  e1=Entry(root)
  e1.place(x=0,y=40,width=238,height=30)
 else:
     l3.config(text=""+str(x))
     l4.config(text="Wrong input!")

def minus():
 global x,e1
 l4.config(text="")
 e3=e1.get()
 if(e3.isnumeric()):
  x-=int(e3)
  l3.config(text=""+str(x))
  e1=Entry(root)
  e1.place(x=0,y=40,width=238,height=30)
 else:
     l3.config(text=""+str(x))
     l4.config(text="Wrong input!")

def reset():
 global x
 l4.config(text="")
 x=0
 l3.config(text=""+str(x))

 
 
 



x=0
l0=Label(root,text="Total:")
l0.place(x=0,y=10,width=70,height=25)

l3=Label(root,text=""+str(x))
l3.place(x=190,y=10,width=70,height=25)

l4=Label(root,text="")
l4.place(x=0,y=120,width=70,height=25)

e1=Entry(root)
e1.place(x=0,y=40,width=238,height=30)

answer=Button(root,text="+",command=plus).place(x=20,y=80,width=30,height=30)
answer=Button(root,text="-",command=minus).place(x=80,y=80,width=30,height=30)
answer=Button(root,text="reset",command=reset).place(x=170,y=80,width=70,height=25)
mainloop()
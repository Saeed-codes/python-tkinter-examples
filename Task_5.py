from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("530x480")
root.title('Order')
bill_size=0
bill_top1=0
bill_top2=0
bill_top3=0
bill_top4=0
bill_top5=0
bill_top6=0
bill_top7=0
total_bill=0


def process():
    global bill_size ,bill_top1,bill_top2,bill_top3,bill_top4,bill_top5,bill_top6,bill_top7,size1,type1,total_bill
    if not size_var.get():
        messagebox.showerror("Incomplete", "Please fill the missing information")
    else:
        size1 = size_var.get()
        if(size1=='S'):
            bill_size=6.5
        else:
            if(size1=='M'):
             bill_size=8.5
            else:
                if(size1=='L'):
                 bill_size=10
                else:
                   bill_size=0 
    if not type_var.get():
        messagebox.showerror("Incomplete", "Please fill the missing information")
    else:
        type1 = type_var.get()
    

    if not type_var.get():
        messagebox.showerror("Incomplete", "Please fill the missing information")
    else:
        type1 = type_var.get()
    if not var1.get():
        bill_top1=0
    else:
        bill_top1=1.5    
#
    if not var2.get():
        bill_top2=0
    else:
        bill_top2=1.5   
#
    if not var3.get():
        bill_top3=0
    else:
        bill_top3=1.5
#
    if not var4.get():
        bill_top4=0
    else:
        bill_top4=1.5
#
    if not var5.get():
        bill_top5=0
    else:
        bill_top5=1.5
#
    if not var6.get():
        bill_top6=0
    else:
        bill_top6=1.5
#
    if not var6.get():
        bill_top6=0
    else:
        bill_top6=0   
    total_bill=bill_size +bill_top1+bill_top2+bill_top3+bill_top4+bill_top5+bill_top6+bill_top7
    label4.config(text="Pizza Type:"+ type_var.get() +"\nPizza Size:"+size_var.get()+"\n Topping:"+var1.get()+""+var2.get()+""+var3.get()+""+var4.get()+""+var5.get()+""+var6.get()+""+var7.get()+"\nAmount Due:"+str(total_bill)).place(x=0,y=320,width=523,height=125)

    
label_0 =Label(root,text="Welcome To Home Style Pizza Shop", width=33,font=("bold",20),foreground='orange')
label_0.place(x=0,y=20)

label_1 =Label(root,text="Each Topping $1", width=20,font=("bold",10),foreground='orange')
label_1.place(x=0,y=80,width=117,height=30)

var1=StringVar()
Checkbutton(root,text="Tomatoes", variable=var1,offvalue="",onvalue="Tomatoes").place(x=15,y=110)
var2=StringVar()
Checkbutton(root,text="Green pepper", variable=var2,offvalue="",onvalue="Green Pepper").place(x=15,y=130)
var3=StringVar()
Checkbutton(root,text="Black Olives", variable=var3,offvalue="",onvalue="Black Olives").place(x=15,y=150)
var4=StringVar()
Checkbutton(root,text="Mushrooms", variable=var4,offvalue="",onvalue="Mushrooms").place(x=15,y=170)
var5=StringVar()
Checkbutton(root,text="Extra Cheese", variable=var5,offvalue="",onvalue="Extra Cheese").place(x=15,y=190)
var6=StringVar()
Checkbutton(root,text="Pepperoni", variable=var6,offvalue="",onvalue="Pepperoni").place(x=15,y=210)
var7=StringVar()
Checkbutton(root,text="Sausage", variable=var7,offvalue="",onvalue="Sausage").place(x=15,y=230)

label_2 =Label(root,text="Pizza Size", width=20,font=("bold",10),foreground='orange')
label_2.place(x=170,y=80,width=117,height=30)

size_var=StringVar()
Radiobutton(root,text="Small 6.50", variable= size_var, value="S").place(x=180,y=110)
Radiobutton(root,text="Medium 8.5", variable= size_var, value="M").place(x=180,y=150)
Radiobutton(root,text="Large 10.5", variable= size_var, value="L").place(x=180,y=190)

label_3 =Label(root,text="Pizza Type", width=20,font=("bold",10),foreground='orange')
label_3.place(x=300,y=80,width=117,height=30)

type_var=StringVar()
Radiobutton(root,text="Thin Crust", variable= type_var, value="Thin Crust").place(x=310,y=110)
Radiobutton(root,text="Medium Crust", variable= type_var, value="Medium Crust").place(x=310,y=150)
Radiobutton(root,text="Pan", variable= type_var, value="Pan").place(x=310,y=190)

Button(root, text='Process Selection' , width=30,bg="light blue",fg='white',command=process).place(x=182,y=230)

label_3 =Label(root,text="Your Order:", width=20,font=("bold",13),foreground='black')
label_3.place(x=0,y=265,width=117,height=30)

label4=Label(root,text="")
label4.place(x=0,y=295)
root.mainloop()
from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("500x500")
root.title('Registration form')
n=0
def save_info():
    global n
    n=n+1
    if not entry_1.get():
        messagebox.showerror("Incomplete", "Please fill the missing information")
    else:
        nameinfo = entry_1.get()
    
    if not entry_3.get():
        messagebox.showerror("Incomplete", "Please fill the missing information")
    else:
        emailinfo = entry_3.get()

    if not var.get():
        messagebox.showerror("Incomplete", "Please fill the missing information")
    else:
        gender = var.get()
    
    if not c.get():
        messagebox.showerror("Incomplete", "Please the missing information")
    else:
        countryinfo = c.get()
    
    if not var1.get():
        if not var2.get():
         messagebox.showerror("Incomplete", "Please the missing information")
        else:
         p1=var1.get()
         p2=var2.get()
    else:
        p1=var1.get()
        p2=var2.get()
    file = open("Data.txt","w")
    file.write("#"+str(n))
    file.write("\n")
    file.write("Name:" + nameinfo)
    file.write("\n")
    file.write("Email: " + emailinfo)
    file.write("\n")
    file.write("Gender: " + gender)
    file.write("\n")
    file.write("Country: " + countryinfo)
    file.write("\n")
    file.write("Programming Languages: " + p1 +" "+ p2)
    file.write("\n")
    file.close()
label_0 =Label(root,text="Registration form", width=20,font=("bold",20))
label_0.place(x=90,y=60)

label_1 =Label(root,text="FullName", width=20,font=("bold",10))
label_1.place(x=80,y=130)

entry_1=Entry(root)
entry_1.place(x=240,y=130)

label_3 =Label(root,text="Email", width=20,font=("bold",10))
label_3.place(x=68,y=180)

entry_3=Entry(root)
entry_3.place(x=240,y=180)

label_4 =Label(root,text="Gender", width=20,font=("bold",10))
label_4.place(x=70,y=230)


var=StringVar()

Radiobutton(root,text="Male",padx= 5, variable= var, value="M").place(x=235,y=230)
Radiobutton(root,text="Female",padx= 20, variable= var, value="F").place(x=290,y=230)

label_5=Label(root,text="Country",width=20,font=("bold",10))
label_5.place(x=70,y=280)

list_of_country=[ 'UAE' ,'US' , 'UK' ,'Germany' ,'Austria']

c=StringVar()
droplist=OptionMenu(root,c, *list_of_country)
droplist.config(width=15)
c.set('Select your Country')
droplist.place(x=240,y=280)

label_6=Label(root,text="Programming Language",width=20,font=('bold',10))
label_6.place(x=75,y=330)

var1=StringVar()

Checkbutton(root,text="Python", variable=var1,offvalue="",onvalue="Python").place(x=230,y=330)


var2=StringVar()
Checkbutton(root,text="Java", variable=var2,offvalue="",onvalue="Java").place(x=290,y=330)

Button(root, text='Submit' , width=20,bg="red",fg='white',command=save_info).place(x=180,y=380)

root.mainloop()
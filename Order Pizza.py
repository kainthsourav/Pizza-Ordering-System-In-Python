
from Tkinter import *
import tkMessageBox
top=Tk()
def o():
    if(E1.get()==0):
        tkMessageBox.showinfo("Message","Fill Name")
    else:
        tkMessageBox.showinfo("Message",E1.get())

    
top.title("Round Pizza Table : The Last Honest Pizza")
canvas=Canvas(width=530,height=150,bg='white')
canvas.pack(expand=YES,fill=BOTH)
gif1=PhotoImage(file='C:\Users\Sourav\Desktop\Project Python\q.gif')
canvas.create_image(50,10,image=gif1,anchor=NW)


frame=Frame(top)
frame.pack(anchor=CENTER,pady=20)
L1=Label(frame, text="Name")
L1.pack()
E1=Entry(frame,bd=5)
E1.pack(pady=5)

mb=  Menubutton (frame,text="Pizaa Type", relief=RAISED )
mb.grid(pady=5)
mb.menu  =  Menu ( mb, tearoff = 0 )
mb["menu"]  =  mb.menu
    
spVar  = IntVar()
mpVar = IntVar()
lpVar = IntVar()


mb.menu.add_checkbutton ( label="Small",
                          variable=spVar)
mb.menu.add_checkbutton ( label="Medium",
                          variable=mpVar )
mb.menu.add_checkbutton ( label="Large",
                          variable=lpVar)

mb.pack(pady=5)

####L2=Label(frame, text="Addrees")
####L2.pack()
####E2=Entry(frame,bd=5)
####E2.pack()
##
##L3=Label(frame, text="Pizaa Type")
##L3.pack()
##E3=Entry(frame,bd=5)
##E3.pack()

L4=Label(frame, text="Mobile Number")
L4.pack()
E4=Entry(frame,bd=5)
E4.pack(pady=5)

L5=Label(frame, text="Email Id")
L5.pack()
E5=Entry(frame,bd=5)
E5.pack(pady=5)

rb=Button(frame,text="Order Now",fg="black",command=o)
rb.pack(side=RIGHT,pady=5)
top.geometry("530x450")
top.resizable(width=False, height=False)
top.mainloop()

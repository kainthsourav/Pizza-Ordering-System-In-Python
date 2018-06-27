from Tkinter import *
from tkMessageBox import *
import sqlite3 
conn = sqlite3.connect('pizza.db')
c = conn.cursor() 

def npiz():
    top.title("Round Pizza Table : The Last Honest Pizza")
    global newpizza
    newpizza=Frame(top)
    newpizza.pack(anchor=CENTER,pady=20)
    global E1,C1,C2,C3,E1,E2,E3,E4,E5,E6,E7
    L1=Label(newpizza, text="Name")
    L1.pack()
    E1=Entry(newpizza,bd=3)
    E1.pack(pady=1)
    L2=Label(newpizza, text="Addrees")
    L2.pack()
    E2=Entry(newpizza,bd=3)
    E2.pack(pady=1)
    L3=Label(newpizza, text="Mobile No")
    L3.pack()
    E3=Entry(newpizza,bd=3)
    E3.pack(pady=1)
    L5=Label(newpizza, text="Small Pizza : Quantity")
    L5.pack()
    E5=Entry(newpizza,bd=3)
    E5.pack(pady=1)
    L6=Label(newpizza, text="Medium Pizza: Quantity")
    L6.pack()
    E6=Entry(newpizza,bd=3)
    E6.pack(pady=1)
    L7=Label(newpizza, text="Large Pizza : Quantity")
    L7.pack()
    E7=Entry(newpizza,bd=3)
    E7.pack(pady=1)
    L4=Label(newpizza, text="Email Id (optional)")
    L4.pack()
    E4=Entry(newpizza,bd=3)
    E4.pack(pady=1)
    rb1=Button(newpizza,text="Back",fg="black",command=hidenewpizza)
    rb1.pack(side=LEFT,pady=1)
    rb2=Button(newpizza,text="Order Now",fg="black",command=save)
    rb2.pack(side=RIGHT,pady=1)
    #top.geometry("530x450")
    #top.resizable(width=False, height=False)
    top.mainloop()

def cpiz():
    top.title("Round Pizza Table : The Last Honest Pizza")
    global cancel,C1,C2
    cancel=Frame(top)
    cancel.pack(anchor=CENTER,pady=20)
    L1=Label(cancel, text="Name")
    L1.pack(pady=5)
    C1=Entry(cancel,bd=5)
    C1.pack()
    L2=Label(cancel, text="Order ID")
    L2.pack(pady=5)
    C2=Entry(cancel,bd=5)
    C2.pack()
    rb2=Button(cancel,text="Back",fg="black",command=hidecp)
    rb2.pack(side=LEFT,pady=10)
    rb=Button(cancel,text="Cancel Now",fg="black",command=ca)
    rb.pack(side=RIGHT,pady=5)
    #top.geometry("530x450")
    #top.resizable(width=False, height=False)
    top.mainloop()
def tp():
    top.title("Round Pizza Table : The Last Honest Pizza")
    global t,f
    t=Frame(top)
    t.pack(anchor=CENTER,pady=20)
    L1=Label(t,text="Order Id")
    L1.pack()
    f=Entry(t,bd=5)
    f.pack(pady=5)
    g=f.get()
    rb2=Button(t,text="Back",fg="black",command=hidet)
    rb2.pack(side=LEFT,pady=10)
    rb=Button(t,text="Track Now",fg="black")
    rb.pack(side=RIGHT,pady=5)
    if(len(g)!=0):
        showinfo('Round Pizza Table','Order will be Served Shortly')
        
    top.mainloop()


def hidenewpizza():
    newpizza.pack_forget()
def hidecp():
    cancel.pack_forget()
def hidet():
    t.pack_forget()
def save():
    name=E1.get()
    ad=E2.get()
    mo=E3.get()
    email=E4.get()
    sp=E5.get()
    mp=E6.get()
    lp=E7.get()
    int_spiz=int(sp)
    int_mpiz=int(mp)
    int_lpiz=int(lp)
    
    order=int_spiz+int_mpiz*2
    print order
   # print (name,ad,mo,email,int_spiz,int_mpiz,int_lpiz,sp,mp,order,lp)
    if(len(name)!=0):
        order=order+1000
        total=(int_spiz*95)+(int_mpiz*195)+(int_lpiz*295)
        print(total)
        #c.execute('CREATE TABLE pizza (orderid int ,name varchar(25), address varchar(30), mobileno int,emailid text,sp int,mpq int,lpq int,total int)')
        c.execute("INSERT INTO pizza (orderid,name,address,mobileno,emailid,sp,mpq,lpq,total) VALUES(?,?,?,?,?,?,?,?,?)",(order,name,ad,mo,email,sp,mp,lp,total))
        print c.execute('SELECT * FROM pizza')
        conn.commit()
        showinfo('Round Pizza Table', \
                                    'Order Placed '
                                    'Order ID :'+' '+ str(order))
        #showinfo('Round Pizza Table : The Last Honest Pizza','Order Placed')

   # if(len(E1.get())!=0 and len(E2.get())!=0 and len(E3.get())!=0 and len(E4.get())==0) and len(E5.get())!=0 and len(E6.get())!=0 and len((E7.get()!=0)):
    #else:
        #print "NAme not ENtered"
def ca():
    name=C1.get()
    order=C2.get()
    if(len(name)!=0):
        c.execute("DELETE FROM pizza WHERE Orderid=?", (order,))
        print c.fetchall()
        #c.execute('DELETE FROM pizza WHERE Name='name' order='order';)
        conn.commit()
        showinfo('Round Pizza Table', \
                                    'Order Canceled ')
    else:
        conn.commit()
        showinfo('Round Pizza Table', \
                                    'Not Found')
    
       



    
        


    
top=Tk()
top.title("Round Pizza Table: Vendor")
canvas=Canvas(width=530,height=150,bg="white")
canvas.pack(expand=YES,fill=BOTH)
gif1=PhotoImage(file='C:\Users\Sourav\Desktop\Project Python\q.gif')
canvas.create_image(50,10,image=gif1,anchor=NW)
frame=Frame(top)
frame.pack(pady=20)
rb=Button(frame,text="ORDER PIZZA",fg="black",command=npiz)
rb.pack(pady=5)
bb=Button(frame,text="CANCEL ORDER",fg="black",command=cpiz)
bb.pack(pady=5)
gb2=Button(frame,text="TRACK ORDER",fg="black",command=tp)
gb2.pack(pady=5)
#top.geometry("530x450")
#top.resizable(width=False, height=False)
top.mainloop()

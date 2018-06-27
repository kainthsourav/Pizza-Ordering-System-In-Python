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
    global E8,E9
    global cancel
    cancel=Frame(top)
    cancel.pack(anchor=CENTER,pady=20)
    L1=Label(cancel, text="Name")
    L1.pack(pady=5)
    E8=Entry(cancel,bd=5)
    E8.pack()
    L2=Label(cancel, text="Order ID")
    L2.pack(pady=5)
    E9=Entry(cancel,bd=5)
    E9.pack()
    rb2=Button(cancel,text="Back",fg="black",command=hidecp)
    rb2.pack(side=LEFT,pady=10)
    rb=Button(cancel,text="Cancel Now",fg="black",command=ca)
    rb.pack(side=RIGHT,pady=5)
    #top.geometry("530x450")
    #top.resizable(width=False, height=False)
    top.mainloop()
def ser():
    global served
    served=Frame(top)
    served.pack(anchor=CENTER,pady=20)
    Label(served, text="Order Id").grid(row=0, column=0,padx=20)
    Label(served, text="Name").grid(row=0, column=1)
    Label(served, text="Address").grid(row=0, column=2)
    Label(served, text="Mobile No").grid(row=0, column=3)
    Label(served, text="Small Pizza").grid(row=0, column=4)
    Label(served, text="Medium Pizza").grid(row=0, column=5)
    Label(served, text="Large Pizza").grid(row=0, column=6)
    Label(served, text="Total").grid(row=0, column=7)
    
    c.execute('SELECT * FROM pizza')
    val=c.fetchall()
    for index, val in enumerate(val):
        c.execute('SELECT * FROM pizza')
        print c.fetchall()
        Label(served, text=val[0]).grid(row=index+1, column=1)
        Label(served, text=val[1]).grid(row=index+1, column=2)
        Label(served, text=val[2]).grid(row=index+1, column=3)
        Label(served, text=val[3]).grid(row=index+1, column=4)
        Label(served, text=val[4]).grid(row=index+1, column=5)
        Label(served, text=val[5]).grid(row=index+1, column=6)
        Label(served, text=val[6]).grid(row=index+1, column=7)
        Label(served, text=val[7]).grid(row=index+1, column=8)
        Label(served, text=val[8]).grid(row=index+1, column=9)

    rb=Button(served,text="Back",fg="black",command=hideser)
    rb.grid(row=6,column=7
            )
def pen():
    global pending
    pending=Frame(top)
    pending.pack(anchor=CENTER,pady=20)
    Label(pending, text="Order Id").grid(row=0, column=0,padx=20)
    Label(pending, text="Name").grid(row=0, column=1)
    Label(pending, text="Address").grid(row=0, column=2)
    Label(pending, text="Mobile No").grid(row=0, column=3)
    Label(pending, text="Small Pizza").grid(row=0, column=4)
    Label(pending, text="Medium Pizza").grid(row=0, column=5)
    Label(pending, text="Large Pizza").grid(row=0, column=6)
    Label(pending, text="Total").grid(row=0, column=7)
    
    c.execute('SELECT * FROM pizza')
    val=c.fetchall()
    for index, val in enumerate(val):
        c.execute('SELECT * FROM pizza')
        print c.fetchall()
        Label(pending, text=val[0]).grid(row=index+1, column=1)
        Label(pending, text=val[1]).grid(row=index+1, column=2)
        Label(pending, text=val[2]).grid(row=index+1, column=3)
        Label(pending, text=val[3]).grid(row=index+1, column=4)
        Label(pending, text=val[4]).grid(row=index+1, column=5)
        Label(pending, text=val[5]).grid(row=index+1, column=6)
        Label(pending, text=val[6]).grid(row=index+1, column=7)
        Label(pending, text=val[7]).grid(row=index+1, column=8)
        Label(pending, text=val[8]).grid(row=index+1, column=9)



    
##    
##    for row in c.execute('SELECT * FROM student3'):
##        print row
    
    
    
##   height = 5
##    width = 5
##    for i in range(height): #Rows
##        for j in range(width): #Columns
##            b = Entry(pending, text="")
##            b.grid(row=i, column=j)
##            b.configure(state='disabled')
##        INSERT INTO Customers (CustomerName, Country)
##SELECT SupplierName, Country FROM Suppliers
##WHERE Country='Germany';

    rb=Button(pending,text="Back",fg="black",command=hidepen)
    rb.grid(row=6,column=9)
    Label(pending, text="Serve Order").grid(row=6, column=5)
    global Q1,oid
    Q1=Entry(pending,bd=5)
    Q1.grid(row=6,column=6)
    rb2=Button(pending,text="Served",fg="black",command=ss)
    rb2.grid(row=6,column=7)
    oid=Q1.get()
    #rb2.grid(row=6,column=7)
def ss():
    if(len(Q1.get())!=0):
        #c.execute('INSERT INTO ser values("Select * FROM pizza WHERE Orderid=?",'(oid,)")))
        rb2=Button(pending,text="Served",fg="black",command=hidepen)
        rb2.grid(row=6,column=7)
        showinfo('Round Pizza Table','Successfull')
    else:
        showinfo('Round Pizza Table','Not Ready')


def hidenewpizza():
    newpizza.pack_forget()
def hidecp():
    cancel.pack_forget()
def hideser():
    served.pack_forget()
def hidepen():
    pending.pack_forget()
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
        #
        
        c.execute("INSERT INTO pizza (orderid,name,address,mobileno,emailid,sp,mpq,lpq,total) VALUES(?,?,?,?,?,?,?,?,?)",(order,name,ad,mo,email,sp,mp,lp,total))
        print c.execute('SELECT * FROM pizza')
        print c.fetchall()
        conn.commit()
        conn.close()
        showinfo('Round Pizza Table', \
                                    'Order Placed '
                                    'Order ID :'+' '+ str(order))
    else:
        conn.commit()
        conn.close()
        showinfo('Round Pizza Table', \
                                    'Not Found')
        #showinfo('Round Pizza Table : The Last Honest Pizza','Order Placed')

   # if(len(E1.get())!=0 and len(E2.get())!=0 and len(E3.get())!=0 and len(E4.get())==0) and len(E5.get())!=0 and len(E6.get())!=0 and len((E7.get()!=0)):
    #else:
        #print "NAme not ENtered"
def ca():
    name=E8.get()
    order=E9.get()
    if(len(name)!=0):
        c.execute("DELETE FROM pizza WHERE Orderid=?", (order,))
        print c.fetchall()
        #c.execute('DELETE FROM pizza WHERE Name='name' order='order';)
        conn.commit()
        conn.close()
        showinfo('Round Pizza Table', \
                                    'Order Canceled ')
    else:
        conn.commit()
        conn.close()
        showinfo('Round Pizza Table', \
                                    'Not Found')


   
        

top=Tk()
top.title("Round Pizza Table: Vendor")
canvas=Canvas(width=500,height=100,bg="white")
canvas.pack(expand=YES,fill=BOTH)
gif1=PhotoImage(file='C:\Users\Sourav\Desktop\Project Python\q.gif')
canvas.create_image(200,10,image=gif1,anchor=NW)
frame=Frame(top)
frame.pack(pady=20)
rb=Button(frame,text="NEW PIZZA ORDER",fg="black",command=npiz)
rb.pack(pady=5)
bb=Button(frame,text="CANCELED ORDER",fg="black",command=cpiz)
bb.pack(pady=5)
gb=Button(frame,text="SERVERD ORDER",fg="black",command=ser)
gb.pack(pady=5)
gb2=Button(frame,text="PENDING ORDER",fg="black",command=pen)
gb2.pack(pady=5)
#top.geometry("530x450")
#top.resizable(width=False, height=False)
top.mainloop()

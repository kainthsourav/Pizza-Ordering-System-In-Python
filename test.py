##from Tkinter import *
##
##class App:
##    def __init__(self,master):
##        self.var = IntVar()
##        frame = Frame(master)
##        frame.grid()
##        f2 = Frame(master,width=200,height=100)
##        f2.grid(row=0,column=1)
##        button = Checkbutton(frame,text='show',variable=self.var,command=self.fx)
##        button.grid(row=0,column=0)
##        msg2="""I feel bound to give them full satisfaction on this point"""
##        self.v= Message(f2,text=msg2)
##    def fx(self):
##        if self.var.get():
##            self.v.grid(column=1,row=0,sticky=N)
##        else:
##            self.v.grid_remove()
##
##top = Tk()
##app = App(top)            
##top.mainloop()
##
##from Tkinter import *
##
##root =Tk()
##root.geometry("500x500")
##root.resizable(width=False, height=False)
##root.mainloop()
from  Tkinter import *
import Tkinter
import tkMessageBox

top=Tkinter.Tk()

frame=Frame(top)
frame.pack()
bottomframe=Frame(top)
bottomframe.pack(side=BOTTOM)
#c=Tkinter.Canvas(top,bg='brown',height=50,width=300)
l1=Label(top,text="enter the pin",bg='blue')
l1.pack(side=LEFT)

v=StringVar()
e1=Entry(top,bd=5,textvariable=v)#textvariable is used taking input from entery
e1.pack(side=LEFT)






def right1():
    down=Tk()
    
    frame1=Frame(down)
    frame1.pack()
    bottomframe1=Frame(down)
    bottomframe1.pack(side=BOTTOM)
    b2=Tkinter.Button(frame1,text="balance enquiry",bg='pink',command=balanceenquiry)
    b2.pack(side=LEFT)
    e2=Entry(frame1,bd=5)
    e2.pack(side=LEFT)
    b3=Tkinter.Button(frame1,text="Deposit",bg='yellow',command=deposit1)
    b3.pack(side=LEFT)
    e3=Entry(frame1,bd=5)
    e3.pack(side=LEFT)
    b4=Tkinter.Button(bottomframe1,text="withdrawl",bg='red',command=withdrawl)
    b4.pack(side=LEFT)
    e4=Entry(bottomframe1,bd=5)
    e4.pack(side=LEFT)

    b5=Tkinter.Button(bottomframe1,text="pinchange",bg='green',command=changepin)
    b5.pack(side=LEFT)

    e5=Entry(bottomframe1,bd=5)
    e5.pack(side=LEFT)
    down.mainloop()
    
    return
def balanceenquiry():
    tkMessageBox.showinfo('balancedetails','balance=500')
    return
def withdrawl():
    withdrawlframe=Tk()
    frame4=Frame(withdrawlframe)
    frame4.pack()
    bottomframe4=Frame(withdrawlframe)
    bottomframe4.pack(side=BOTTOM)
    b12=Tkinter.Button(frame4,text="enter the amount",bg='pink')
    b12.pack(side=LEFT)

    e12=Entry(frame4,bd=5)
    e12.pack(side=LEFT)
    b11=Tkinter.Button(bottomframe4,text="submit",bg='grey',command=withdrawl1)
    b11.pack(side=BOTTOM)
    return
def withdrawl1():
    tkMessageBox.showinfo('withdrawldetails','collect the amount')
   
def deposit1():
    depositframe=Tk()
    frame3=Frame(depositframe)
    frame3.pack()
    bottomframe3=Frame(depositframe)
    bottomframe3.pack(side=BOTTOM)
    b9=Tkinter.Button(frame3,text="enter the amount",bg='pink')
    b9.pack(side=LEFT)
    e6=Entry(frame3,bd=5)
    e6.pack(side=LEFT)
    b14=Tkinter.Button(depositframe,text="submit",bg='grey',command=deposit2)
    b14.pack(side=BOTTOM)
    return
def deposit2():
    depositframe1=Tk()
    frame5=Frame(depositframe1)
    frame5.pack()
    b10=Tkinter.Button(frame5,text="Deppsit the amount",bg='yellow')
    b10.pack(side=LEFT)
    e7=Entry(frame5,bd=5)
    e7.pack(side=LEFT)
    b11=Tkinter.Button(depositframe1,text="submit",bg='grey',command=deposit3)
    b11.pack(side=BOTTOM)
def deposit3():
    tkMessageBox.showinfo('depositdetils','depositdone')
    
    return

def wrong1():
    print 'sorry'
def pin():
    p=StringVar()
    v=e1.get()
    p="1234"
    if (v==p):
        right1()
    else:
        wrong1()
        print v
    return
def changepin():
    middle=Tk()
    frame2=Frame(middle)
    frame2.pack()
    bottomframe2=Frame(middle)
    bottomframe2.pack(side=BOTTOM)
    l6=Label(frame2,text='oldpin',bg='red')
    l6.pack(side=LEFT)
    e6=Entry(frame2,bd=5)
    e6.pack(side=LEFT)
    l7=Label(frame2,text='newpin',bg='yellow')
    l7.pack(side=LEFT)
    e7=Entry(frame2,bd=5)
    e7.pack(side=LEFT)
    l8=Label(frame2,text='reenterpin',bg='pink')
    l8.pack(side=LEFT)
    e8=Entry(frame2,bd=5)
    e8.pack(side=LEFT)
    b6=Tkinter.Button(bottomframe2,text="confirm",bg='green',command=changepin1)
    b6.pack(side=BOTTOM)
    middle.mainloop()
    return
def changepin1():
    tkMessageBox.showinfo('pindetails','changingpin has done sucessfully')
     
    
#def wish():
   # print 'you have chaged your pin'
b1=Tkinter.Button(bottomframe,text='submit',bg='green',command=pin)
b1.pack(side=BOTTOM)
#c.pack()
top.mainloop()



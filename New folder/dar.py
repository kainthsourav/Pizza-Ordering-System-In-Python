from Tkinter import *
import sqlite3 
conn = sqlite3.connect('pizza.db')
c = conn.cursor()
def showallrecords(self):
    self.master=master
    self.master.geometry('250x200+100+200')
    self.master.title('Records')
    data = self.readfromdatabase()
    for index, dat in enumerate(data):
        Label(self.master, text=dat[0]).grid(row=index+1, column=0)
        Label(self.master, text=dat[1]).grid(row=index+1, column=1)
        Label(self.master, text=dat[2]).grid(row=index+1, column=2)
def readfromdatabase(self):
    self.cur.execute("SELECT * FROM pizza")
    return self.cur.fetchall()




showallrecords(a)
readfromdatabase(a)

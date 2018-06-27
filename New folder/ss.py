##from Tkinter import *
##from tkMessageBox import *
##
##def answer():
##    showerror("Answer", "Sorry, no answer available")
##
##def callback():
##    if askyesno('Verify', 'Really quit?'):
##        showwarning('Yes', 'Not yet implemented')
##    else:
##        showinfo('No', 'Quit has been cancelled')
##
##Button(text='Quit', command=callback).pack(fill=X)
##Button(text='Answer', command=answer).pack(fill=X)
##mainloop()
from Tkinter import * #If you get an error here, try Tkinter not tkinter

def Dialog1Display():
    Dialog1 = Toplevel(height=100, width=100) #Here

def Dialog2Display():
    Dialog2 = Toplevel(height=1000, width=1000) #Here

master=Tk()

Button1 = Button(master, text="Small", command=Dialog1Display)
Button2 = Button(master, text="Big", command=Dialog2Display)

Button1.pack()
Button2.pack()
master.mainloop()

from Tkinter import *

class Alarm(Frame):
    def repeater(self):                 
        self.bell()                     
        self.stopper.flash()            
        self.after(self.msecs, self.repeater) 
    def __init__(self, msecs=1000):           
        Frame.__init__(self)
        self.msecs = msecs
        self.pack()
        stopper = Button(self, text='Stop the beeps!', command=self.quit)
        stopper.pack()
        stopper.config(bg='navy', fg='white', bd=8) 
        self.stopper = stopper
        self.repeater()


class AlarmWithDraw(Alarm):
    def repeater(self):                           
        self.bell()                               
        if self.master.state() == 'normal':       
            self.master.withdraw()                
        else:                                     
            self.master.deiconify()               
            self.master.lift()                    
        self.after(self.msecs, self.repeater)     

if __name__ == '__main__': AlarmWithDraw().mainloop()

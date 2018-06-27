from Tkinter import *
root=Tk()
class Window(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.master=master
        self.func()

def func(self):
    self.count=0
    self.op_row=0
    button=Button(self.master,text="Add",command= self.func_op)
    button.grid(column=0,row=0)
    label=Label(self,text="Welcome")
    label.grid(column=0,row=0)

    def func_op(self):
        self.count=self.count+1
        self.op_row=self.op_row+1
        self.var=StringVar()
        options=["a","b","c"]
        op=OptionMenu(self.master,self.var,*options)
        op.grid(column=0,row=self.op_row)

if __name__ == "__main__":
    root = Tk()
    aplication = Window(root)
    root.mainloop()   

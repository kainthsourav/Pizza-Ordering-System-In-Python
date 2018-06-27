from Tkinter import *

root = Tk()


def opt1():
    print "opt 1 selected "
    return;
def opt2():
    print "opt 2 selected "
    return;
def opt3():
    print "opt 3 selected "
    return;

elementTypeBtn = Menubutton(root, relief='raised', text='select sth')
elementTypeBtn.grid(row=0, column=0)
elementTypeBtn.menu = Menu(elementTypeBtn)
elementTypeBtn.menu.add_command(label='opt1', underline=0, command=opt1)
elementTypeBtn.menu.add_command(label='opt2', underline=0, command=opt2)
elementTypeBtn.menu.add_command(label='opt3', underline=0, command=opt3)
elementTypeBtn['menu'] = elementTypeBtn.menu

def opt1():
    elementTypeBtn = Menubutton(root, relief='raised', text='select sth')
    elementTypeBtn.grid(row=0, column=0)


root.mainloop()

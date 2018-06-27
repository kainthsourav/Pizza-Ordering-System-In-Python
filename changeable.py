#Use a StringVar to create a changeable label
from Tkinter import*

#Hold onto a global reference for the root window
root=None

#changeable text that that will go inside the label
myText=None
count=0 #click counter

def buttonPushed():
	global myText
	global count
	count +=1
	myText.set("Stop Clicking, it's already been %d times!" %(count))

def addTextLabel(root):
	global myText
	myText=StringVar()
	myText.set("")
	myLabel=Label(root,textvariable=myText)
	myLabel.pack()

def main():
	global root
	root=Tk()#Create the root (base) window where all widgets go
	myButton=Button(root,text="Show Text",command=buttonPushed)
	myButton.pack()
	addTextLabel(root)
	root.mainloop() # Start the event loop

main()

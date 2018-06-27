class Welcome():
#This is the class defining the first welcoming window. This window is used to navigate between previous weights and the calculator.
     def __init__(self,master):
        #This is the GUI for the starting Menu area. Features three buttons for navigating towards the BMI Calculator, the Records where we have to store variables entered and the exit# 

          self.master=master
          self.master.geometry('170x110+100+200')
          self.master.title('Welcome!')

          self.label1=Label(self.master,text='Welcome to the BMI Calculator',fg='red').grid(row=0,column=1)
          self.button1=Button(self.master,text="BMI Calculator",fg='green',command=self.gotobmicalculator).grid(row=1,column=1)
          self.button2=Button(self.master,text="Records",fg='blue',command=self.gotorecords).grid(row=2,column=1)
          self.button3=Button(self.master,text="Exit",fg='red',command=self.exit).grid(row=3,column=1)

     def exit(self):
        #Exit protocol for the exit button. This part is completely done.#
          self.master.destroy()

     def gotobmicalculator(self):
        #This is the BMI Calculator GUI#    
          root2=Toplevel(self.master)
          myGUI=bmicalculator(root2)

     def gotorecords(self):
        #This is where the previous records of BMI will be kept, hasn't been put in yet#
          root2=Toplevel(self.master)
          mygui=records(root2)

class bmicalculator():
     #class created for the bmi calculator GUI and processing the numbers (pain in the ass to make)#
     def __init__(self,master):

          c.execute('CREATE TABLE IF NOT EXISTS BMIStorage(timestamp TEXT,bodymassindex REAL,weightclass TEXT)') 

          self.heightcm=DoubleVar()
          self.weightkg=DoubleVar()

          self.master=master
          self.master.geometry('250x200+100+200')
          self.master.title('BMI Calculator')

          self.label2=Label(self.master,text='Welcome to the BMI Calculator',fg='red').grid(row=0,column=0)
          self.label2=Label(self.master,text='Please enter your height in centimetres',fg='black').grid(row=3,column=0)
          self.label2=Label(self.master,text='Please enter your weight in kilograms',fg='black').grid(row=4,column=0)

          self.myheight=Entry(self.master,textvariable=self.heightcm).grid(row=3,column=1)
          self.myweight=Entry(self.master,textvariable=self.weightkg).grid(row=4,column=1)
          self.button4=Button(self.master,text="Calculate BMI",fg='red',command=self.bmicalculation).grid(row=7,column=0)
          self.button5=Button(self.master,text="Exit",fg='red',command=self.exit).grid(row=9,column=0)

     def bmicalculation(self):
          bmiheight=self.heightcm.get()
          print bmiheight
          bmiweight=self.weightkg.get()
          bmi= float((bmiweight)/((bmiheight / 100)**2))
          self.bmi = bmi
          print bmi
          self.label1=Label(self.master,text='Your BMI is %.2f' % bmi).grid(row=5,column=0)

          if bmi <= 18.5:
               self.label2=Label(self.master,text='This places you in the underweight group.',fg='blue').grid(row=6,column=0)
               totalindex = 'underweight'
               self.totalindex = totalindex
          elif bmi >18.5 and bmi <25:
               self.label3=Label(self.master,text='This places you in the healthy weight group.',fg='green').grid(row=6,column=0)
               totalindex = 'healthy'
               self.totalindex = totalindex
          elif bmi >= 25 and bmi < 30:
               self.label4=Label(self.master,text='This places you in the overweight group.',fg='orange').grid(row=6,column=0)
               totalindex = 'overweight'
               self.totalindex = totalindex
          elif bmi >=30:
               self.label5=Label(self.master,text='This places you in the obese group.',fg='red').grid(row=6,column=0)
               totalindex = 'obese'
               self.totalindex = totalindex

          if bmi >0 and bmi <999999999999999999999:
               self.button6=Button(self.master,text="Store Data",fg='red',command=self.dynamic_data_entry).grid(row=8,column=0)

     def dynamic_data_entry(self):
          global dynamic_data_entry
        #this is what adds the data to the database. Bmi has to be changed to the value of bmi and weightclass has to be change to the weightclass
          timestamp = str(datetime.datetime.now().date())
          bodymassindex = self.bmi
          weightclass = self.totalindex
          c.execute("INSERT INTO BMIStorage (timestamp, bodymassindex, weightclass) VALUES (?, ?, ?)",(timestamp, bodymassindex, weightclass))
          conn.commit()
          self.writetodatabase()

     def writetodatabase(self):
          for i in range(1):
               time.sleep(1)
          c.close()
          conn.close()

     def exit(self):
          #Exit protocol for the exit button. This part is completely done.#
          self.master.destroy()

class records():
     #class created to see records that have been previously inputted#
     def __init__(self,master):
          self.master=master
          self.master.geometry('250x200+100+200')
          self.master.title('Records')






def main():
     root=Tk()
     myGUIWelcome=Welcome(root)
     root.mainloop()

if __name__ == '__main__':
     main()

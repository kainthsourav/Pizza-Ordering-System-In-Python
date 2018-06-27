class App:
    def __init__(self,master):
        frame = Frame(master)
        frame.pack()
        a = StringVar()
        b = StringVar()
        a1 = StringVar()
        b1 = StringVar()
        c = StringVar()
        self.button=Button(frame, \ text="Open Db", \ fg="red", \ command=self.ouvrir)
        self.button.pack(side=LEFT) self.button2=Button(frame, \ text="create table", \ command=self.tabluh)
        self.button2.pack(side=LEFT) self.button3=Button(frame, text= \ "Close DBase", \ command=self.fermer)
        self.button3.pack(side=LEFT) self.button4=Button(frame, text='Insert Rec', \ command= \ self.insertar)
        self.button4.pack(side=LEFT) self.button5 = Button(frame, \ text = 'List Recs', \ command=self.listar)
        self.button5.pack(side=LEFT)
        self.a = Entry(frame) self.a.pack(side=BOTTOM) self.b = Entry(frame)
        self.b.pack(side=BOTTOM) self.c = Entry(frame) self.c.pack(side=BOTTOM)
        def ouvrir(self):
            self.con=sqlite3.connect('maddb')
            self.cur = self.con.cursor()
        def tabluh(self):
                self.cur=self.con.cursor() self.cur.execute('''CREATE TABLE xxx( id INTEGER, fn stringvar(10), ln stringvar(10))''')
        def fermer(self): self.con.close()
        def insertar(self):
            a1 = self.a.get()
            b1 = self.b.get()
            c1 = int(self.c.get())
            self.cur.execute \("insert into \ xxx (id, fn, ln) \ values (?, ?, ?)", \ (c1, a1, b1)) # end of new code self.con.commit() def listar(self): self.cur.execute('SELECT * FROM xxx') print(self.cur.fetchall())
# previous testing of data #a1 = self.a.get() #b1 = self.b.get() #print(a1,b1)
# end of previous testing

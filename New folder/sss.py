import sqlite3 
conn = sqlite3.connect('pizza.db')
c = conn.cursor()
print c.execute('SELECT * FROM pizza')
c.execute("INSERT INTO pizza (orderid,name,address,mobileno,emailid,sp,mpq,lpq,total) VALUES('ORDER_ID','NAME','ADDRESS','MOBLIE NO','EMAIL','SMALL PIZZA','MEDIUM PIZZA','LARGE PIZZA','TOTAL')")
print c.fetchone()


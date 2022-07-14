import mysql.connector as conn

mydb = conn.connect(host="localhost", user="root", passwd="Root@123")
cursor = mydb.cursor()

s = "insert into harish.ineuron1 values(101 , 'Sanket Mane' , 'sanket@gmail.com' , 100 , 30)"
cursor.execute(s)
cursor.execute(s)

mydb.commit()

cursor.execute("select *  from harish.ineuron1 ")
for i in cursor.fetchall():
    print(i)
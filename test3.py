import mysql.connector as conn

mydb = conn.connect(host="localhost", user="root", passwd="Root@123")
cursor = mydb.cursor()

cursor.execute("select employe_id , emp_mailid from harish.ineuron1")
for i in cursor.fetchall():
    print(i)
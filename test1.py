import mysql.connector as conn

mydb = conn.connect(host="localhost", user="root", passwd="Root@123")

print(mydb)

cursor = mydb.cursor()
# cursor.execute("create database harish")
cursor.execute("show databases")
print(cursor.fetchall())


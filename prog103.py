#update a Record
import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="pythondb2")
mycursor=mydb.cursor()

mycursor.execute("update emp set ename='Ashish Varma',sal=13300 where eid=101")

mydb.commit()

print(mycursor.rowcount,"record(s) updated")
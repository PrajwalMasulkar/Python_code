#Insert Into Table
import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="pythondb")
mycursor=mydb.cursor()

sql="INSERT INTO emp VALUES(101,'Ashish',9990)"
mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount," Record inserted.")
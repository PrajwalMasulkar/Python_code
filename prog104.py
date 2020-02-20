#Select specific records
import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="pythondb")
mycursor=mydb.cursor()

mycursor.execute("SELECT * FROM emp where ename='Ashish Varma'")

myresult=mycursor.fetchall()

for x in myresult:
 print(x)
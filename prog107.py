#Select specific records
import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="pythondb3")
mycursor=mydb.cursor()

mycursor.execute("SELECT * FROM Student where Rollno='65599'")

myresult=mycursor.fetchall()

for x in myresult:
 print(x)
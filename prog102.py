#Delete records from the table
import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="pythondb")
mycursor=mydb.cursor()

mycursor.execute("delete FROM emp")

mydb.commit()

print(mycursor.rowcount,"Record(s)deleted")
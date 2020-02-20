import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="pythondb3")
mycursor=mydb.cursor()

mycursor.execute("CREATE TABLE Student(Rollno int(10),Sname VARCHAR(20),Course VARCHAR(20),Phone VARCHAR(10),Email VARCHAR(20))")
print("Table Created Successfully...")
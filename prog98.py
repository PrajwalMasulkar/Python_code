#Creating a Table
import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="pythondb3")
mycursor=mydb.cursor()

mycursor.execute("CREATE TABLE emp(eid int(10),ename VARCHAR(20),sal int(10))")
print("Table Created Successfully....")
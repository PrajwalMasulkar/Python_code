#Create a Database
import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",passwd="")
mycursor=mydb.cursor()

mycursor.execute("CREATE DATABASE pythondb2")
print("Database Created Successfully....")
#if this page is executed with no error,you have successfully Created a database.

#Return a list of your Mysql databases:
import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="")
mycursor=mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
 print(x)
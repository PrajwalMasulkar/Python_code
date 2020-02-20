import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="pythondb3")
mycursor=mydb.cursor()

sql="INSERT INTO Student VALUES(65599,'Prajwal','AI',80852825325,'prajwalmasulkar75@gmail.com')"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount,"Record Inserted")

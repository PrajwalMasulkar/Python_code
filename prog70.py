# placeholder of self in class and Object

class Stud:
 def __init__ (myself,name,age):
  myself.name=name
  myself.age=age
 def show(yourself):
  print("Hello, My name is "+yourself.name)
  
ob=Stud("Dev",21)
ob.show()
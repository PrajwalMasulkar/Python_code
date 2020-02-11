# methods in Class and Object

class Stud:
 def __init__(self,name,age):
  self.name=name
  self.age=age
 def show(self):
  print("Hello, My name is "+self.name)
  
ob=Stud("Dev",21)
ob.show()
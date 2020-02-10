#__init()__ in Class and Object [used to initialize class variable]
# 'self' is a referance like 'this'

class Stud:
 def __init__(self,nm,ag): #__init__() function like constructor
  self.name=nm
  self.age=ag
  
ob=Stud("dev",21)
print(ob.name)
print(ob.age)
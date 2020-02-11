#Data-member modification using object

class Stud:
 def __init__(myself,name):
  myself.name=name
 def show(yourself):
  print("Hello,My name is "+yourself.name)
  
ob=Stud("Dev")
ob.show()
ob.name="Ashish"
ob.show()
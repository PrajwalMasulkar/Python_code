# delete Data-member

class Stud:
 def __init__(myself,name):
  myself.name=name
 def show(yourself):
  print("Hello,My Name is "+yourself.name)
  
ob=Stud("Dev")
ob.show()
del ob.name
ob.show()
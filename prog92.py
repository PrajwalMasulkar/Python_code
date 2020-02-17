#Check if file exist,then delete it using FileHandling

import os

if os.path.exists("myfile1.txt"):
 os.remove("myfile1.txt")
 print("File Removed Successfully..")
else:
 print("The file does not exists")
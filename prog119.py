#creating a GUI App with Message [same as label]

from tkinter import *

main= Tk()
ourMessage ='This is our Message'
ob = Message(main, text = ourMessage)
ob.config(bg='lightgreen')
ob.pack()
main.mainloop()
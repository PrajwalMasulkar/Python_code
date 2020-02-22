#creating a GUI App with Entry [Textbox]

from tkinter import *

master = Tk()
Label(master, text='First Name').grid(row=0, column=0)
Label(master, text='Last name').grid(row=1, column=0)
e1 = Entry(master)
e2 = Entry(master)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
mainloop()
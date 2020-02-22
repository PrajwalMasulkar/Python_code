#creating a GUI App with Menu

from tkinter import *

top = Tk()
mb = Menubutton( top, text = "Menu")
mb.grid()
mb.menu = Menu( mb, tearoff = 0 )
mb["menu"] = mb.menu
a = IntVar()
b = IntVar()
mb.menu.add_checkbutton ( label = 'Contact', variable = a )
mb.menu.add_checkbutton ( label = 'About',variable = b )
mb.pack()
top.mainloop()


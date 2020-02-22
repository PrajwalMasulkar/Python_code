#creating a GUI App with Menu

from tkinter import * 

root = Tk()
mob = Menu(root)
root.config(menu=mob)

filemenu = Menu(mob)
mob.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='open')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)

helpmenu = Menu(mob)
mob.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About')

mainloop()
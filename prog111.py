#creating a GUI App with object

import tkinter as tk

r=tk.Tk()
w=tk.Canvas(r, width=400,height=600)
w.pack()
w.create_line(10,20,400,400 )
r.mainloop()
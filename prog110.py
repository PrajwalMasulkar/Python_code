#creating a GUI App with Button

import tkinter as tk

r=tk.Tk()
r.title('My Frame')
button=tk.Button(r,text='Stop',width=25,command=r.destroy)
button.pack()
r.mainloop()
#creating a GUI App with Frame [Container To Hold the controls]

from tkinter import *

root = Tk()

frame = Frame(root)
frame.pack()
redbutton = Button(frame, text = 'Red', fg='red')
redbutton.pack( side=LEFT)
greenbutton = Button(frame, text = 'Brown',fg='brown')
greenbutton.pack( side = LEFT )
bluebutton = Button(frame, text ='Blue', fg ='blue')
bluebutton.pack(side = LEFT)


bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )
blackbutton = Button(bottomframe, text ='Black', fg='black')
blackbutton.pack( side = BOTTOM)

root.mainloop()
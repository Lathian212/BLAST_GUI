'''
Created on Oct 12, 2015

@author: Lathian
'''
from tkinter import *

def sel():
    selection = "You selected the option " + str(var.get())
    label.config(text = selection)

root = Tk()
var = IntVar()
R1 = Radiobutton(root, text="Option 1", variable=var, value=1,
                  command=sel)
R1.grid(row = 0, column = 0)

R2 = Radiobutton(root, text="Option 2", variable=var, value=2,
                  command=sel)
R2.grid(row = 0, column = 1)

R3 = Radiobutton(root, text="Option 3", variable=var, value=3,
                  command=sel)
R3.grid(row = 0, column = 2)

label = Label(root)
label.grid (row =1 , columnspan =2)
root.mainloop()
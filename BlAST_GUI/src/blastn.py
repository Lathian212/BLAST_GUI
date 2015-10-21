'''
Created on Oct 20, 2015

@author: Lathian
There are 5 main BLAST+ interfaces I need to implement although there additional ones.
Those are blastn, blastp, blastx, tblastn, and tblastx.
I will try a top down approach, focusing on the GUI frontend and the hooks I need to
get out data before defining the method handlers and the subprocess command I will
need to execute the command.

I will use the grid widget geometry manager as this is basically a table entry form.

This is blastn.
'''
import tkinter as tk
from scrollableCanvas import ScrCan
#Globals
#Row needs to be kept track of so code can be moved around and all the griding doesn't need to be adjust
ROW = 0
#Attached to radio buttons for switching between Blast types.



#Functions
def makeVSpace(parent):
    """Makes a blank space in the grid with a label otherwise geometry manager collapses space"""
    global ROW
    tk.Label(parent, text='').grid(row=ROW, column=0)
    ROW += 1
def blastSwitch():
    """Method to switch between blast types"""
    print ( "You selected the option " + str(blastRadio.get()))
    #Unfinished need to destroy scrCanvas and replace it in another file



#Widget Layout

"""Pop up a Tk root window and make Scrollable Canvas it's child"""
root = tk.Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
scrCanvas = ScrCan(root)



#Get inner frame from scrCanvas
blastnFrm = scrCanvas.frame
#Put in spaces and identify type of Blast.
makeVSpace(blastnFrm)
makeVSpace(blastnFrm)
tk.Label(blastnFrm, text='NCBI/ BLAST+/ blastn suite', font=('Arial', '10')).grid(row = ROW , column = 0, columnspan=2)
ROW += 1

#Make Horizontal radio buttons to control switching between program sets.
blastRadio = tk.IntVar()
R1 = tk.Radiobutton(blastnFrm, text="blastn", font=('Arial', '12'), variable=blastRadio, value=1, command=blastSwitch)
R1.grid(row = ROW, column = 0)
R2 = tk.Radiobutton(blastnFrm, text="blastn", font=('Arial', '12'), variable=blastRadio, value=2, command=blastSwitch)
R2.grid(row = ROW, column = 1)
R3 = tk.Radiobutton(blastnFrm, text="blastn", font=('Arial', '12'), variable=blastRadio, value=3, command=blastSwitch)
R3.grid(row = ROW, column = 2)
R4 = tk.Radiobutton(blastnFrm, text="blastn", font=('Arial', '12'), variable=blastRadio, value=4, command=blastSwitch)
R4.grid(row = ROW, column = 3)
R5 = tk.Radiobutton(blastnFrm, text="blastn", font=('Arial', '12'), variable=blastRadio, value=5, command=blastSwitch)
R5.grid(row = ROW, column = 4)
blastRadio.set(1)
ROW += 1

makeVSpace(blastnFrm)

tk.Label(blastnFrm, text='Enter Query Sequence', font=('Arial', '14')).grid(row = ROW , column = 0, columnspan=4)
ROW += 1
tk.Label(blastnFrm, text='Enter accession number(s), gi(s), or FASTA sequence(s)', font=('Arial', '12', 'bold')).grid(row = ROW , column = 0, columnspan=4)

ROW += 1



root.mainloop()


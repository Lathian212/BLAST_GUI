'''
Created on Oct 20, 2015

@author: Lathian
There are 5 main_bk BLAST+ interfaces I need to implement although there additional ones.
Those are blastn, blastp, blastx, tblastn, and tblastx.
I will try a top down approach, focusing on the GUI frontend and the hooks I need to
get out data before defining the method handlers and the subprocess command I will
need to execute the command.

I will use the grid widget geometry manager as this is basically a table entry form.

This is blastn.
'''
import tkinter as tk
from ScrollableCanvas import ScrollableCanvas 
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
class Tblastx:
    #Attached to radio buttons for switching between Blast types.
    def __init__(self, scrFrame):
        #Globals
        #Save a reference to canvas_frame so this class' frame can be destroyed and recreated.
        self.scrFrame = scrFrame
        #self.ROW needs to be kept track of so code can be moved around and all the griding doesn't need to be adjusted
        #It gets its value from the RadioController object.
        self.ROW = 0
    
    #Functions
    def destroyInnerF(self):
        """ Destroy method works but I cannot as of yet get forget to work possibly due to interactive nature of GUI """
        self.inFrm.destroy()
    def buildInnerF(self):
        """ Builds all the widgets for blastn suite, it adds things either of two check boxes are selected """
        self.inFrm = tk.Frame(self.scrFrame)
        #Reset ROW to control layout in blast inner frame
        self.ROW = 0
        self.buildBlock1()
        self.inFrm.grid(row = 1, column = 0)
    def makeVSpace(self, parent):
        """Makes a vertical blank space in the grid with a label otherwise geometry manager collapses space"""
        tk.Label(parent, text = '').grid(row=self.ROW, column=1)
        self.ROW += 1
    def makeHSpace(self, parent, r, c = 0, width = 5):
        """Make a horizontal blank space which otherwise grid manager collapses."""
        spacer = ' ' * width
        tk.Label(parent, text =  spacer).grid(row = r, column = c)
    #Widget Layout
    def buildBlock1(self):        
        self.makeVSpace(self.inFrm)
        #Left side padding
        tk.Label(self.inFrm, text = '     ').grid(row = self.ROW, column = 0, rowspan = 1000)
        self.ROW+=1
        tk.Label(self.inFrm, text = 'Tblastx filler', font =('Arial', 16, 'bold')).grid(row = self.ROW, column =1)
        

 









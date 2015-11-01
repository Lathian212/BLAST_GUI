'''
Created on Nov 1, 2015

@author: Lathian
This Class Instantiates the 5 Blast pages and controls switching among them
'''
import tkinter as tk
import Blastn
import Blastp
import Blastx
import Tblastn
import Tblastx


class RadioController:
    def __init__(self, scrFrame):
        #Globals
        #self.ROW needs to be kept track of so code can be moved around and all the griding doesn't need to be adjust
        self.ROW = 0
        #Save a reference to canvas_frame 
        self.scrFrame = scrFrame
        #Create an inner frame to keep consistent with other code
        self.inFrm = tk.Frame(self.scrFrame)
        #Create radio buttons
        self.buildHeader()
        #Grid it onto the scrollable frame
        self.inFrm.grid(row = 0, column =0)
        #Create all the Blast objects just don't invoke their build methods.
        """
        self.blastn = Blastn(scrFrame, self.ROW)
        self.blastp = Blastp(scrFrame, self.ROW)
        self.blastx = Blastx(scrFrame, self.ROW)
        self.tblastn = Tblastn(scrFrame, self.ROW)
        self.tblastx = Tblastx(scrFrame, self.ROW)
        #Set current_blast to blastn and invoke it's build method
        self.current_blast = self.blastn
        self.current_blast.buildInnerF()
        """
        
    def makeVSpace(self, parent):
        """Makes a vertical blank space in the grid with a label otherwise geometry manager collapses space"""
        tk.Label(parent, text = '').grid(row=self.ROW, column=1)
        self.ROW += 1
    def makeHSpace(self, parent, r, c = 0, width = 5):
        """Make a horizontal blank space which otherwise grid manager collapses."""
        spacer = ' ' * width
        tk.Label(parent, text =  spacer).grid(row = r, column = c)
    def blastSwitch(self):
        self.current_blast.destroyInnerF()
        r_val = self.radio.get()
        if (r_val == 1):
            pass
        elif (r_val == 2):
            pass
        elif (r_val == 3):
            pass
        elif (r_val == 4):
            pass
        elif (r_val == 5):
            pass
        
    
    def buildHeader(self):
                #Put in spaces and identify type of Blast.
        self.makeVSpace(self.inFrm)
        self.makeVSpace(self.inFrm)
        #Left side padding
        tk.Label(self.inFrm, text = '     ').grid(row = self.ROW, column = 0, rowspan = 1000) 
        self.prg_label = tk.Label(self.inFrm, text='NCBI/ BLAST+/ blastn suite',  font=('Arial', '10'))
        self.prg_label.grid(row = self.ROW , column = 1, columnspan=2)
        #Handle to change label when radio button switched
        self.prg_identity = tk.StringVar()
        self.prg_label.configure(textvariable = self.prg_identity)
        self.ROW += 1
        
        #Make Horizontal radio buttons to control switching between program sets.
        self.makeHSpace(self.inFrm, self.ROW)
        self.radio = tk.IntVar()
        R1 = tk.Radiobutton(self.inFrm, text="blastn", font=('Arial', '12'), variable=self.radio, value=1, command=self.blastSwitch)
        R1.grid(row = self.ROW, column = 1)
        R2 = tk.Radiobutton(self.inFrm, text="blastp", font=('Arial', '12'), variable=self.radio, value=2, command=self.blastSwitch)
        R2.grid(row = self.ROW, column = 2)
        R3 = tk.Radiobutton(self.inFrm, text="blastx", font=('Arial', '12'), variable=self.radio, value=3, command=self.blastSwitch)
        R3.grid(row = self.ROW, column = 3)
        R4 = tk.Radiobutton(self.inFrm, text="tblastn", font=('Arial', '12'), variable=self.radio, value=4, command=self.blastSwitch)
        R4.grid(row = self.ROW, column = 4)
        R5 = tk.Radiobutton(self.inFrm, text="tblastx", font=('Arial', '12'), variable=self.radio, value=5, command=self.blastSwitch)
        R5.grid(row = self.ROW, column = 5)
        #Initially toggle blastn as on
        self.radio.set(1)
        self.ROW += 1
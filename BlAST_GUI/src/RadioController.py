'''
Created on Nov 1, 2015

@author: Lathian
This Class Instantiates the 5 Blast pages and controls switching among them
'''
import tkinter as tk
import Blastn as bn
import Blastp as bp
import Blastx as bx
import Tblastn as tbn
import Tblastx as tbx


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
        self.ROW = self.buildHeader(self.ROW)
        #Grid it onto the scrollable frame
        self.inFrm.grid(row = 0, column =0)
        #Create all the Blast objects just don't invoke their build methods.
        
        self.blastn = bn.Blastn(scrFrame, self.ROW)
        self.blastp = bp.Blastp(scrFrame, self.ROW)
        self.blastx = bx.Blastx(scrFrame, self.ROW)
        self.tblastn = tbn.Tblastn(scrFrame, self.ROW)
        self.tblastx = tbx.Tblastx(scrFrame, self.ROW)
        #Set current_blast to blastn and invoke it's build method
        self.current_blast = self.blastn
        self.current_blast.buildInnerF()
        
    def makeVSpace(self, parent):
        """Makes a vertical blank space in the grid with a label otherwise geometry manager collapses space"""
        tk.Label(parent, text = '').grid(row=self.ROW, column=1)
        self.ROW += 1
    def makeHSpace(self, parent, r, c = 0, width = 5):
        """Make a horizontal blank space which otherwise grid manager collapses."""
        spacer = ' ' * width
        tk.Label(parent, text =  spacer).grid(row = r, column = c)
    def blastSwitch(self):
        #Destroy frame containing widgets of active blast suite
        #Note this might be done with the forget method more efficiently investigate.
        self.current_blast.destroyInnerF()
        r_val = self.radio.get()
        if (r_val == 1):
            self.prg_identity.set('NCBI/ BLAST+/ blastn suite' )
            self.current_blast = self.blastn
        elif (r_val == 2):
            self.prg_identity.set('NCBI/ BLAST+/ blastp suite' )
            self.current_blast = self.blastp
        elif (r_val == 3):
            self.prg_identity.set('NCBI/ BLAST+/ blastx suite' )
            self.current_blast = self.blastx
        elif (r_val == 4):
            self.prg_identity.set('NCBI/ BLAST+/ tblastn suite' )
            self.current_blast = self.tblastn
        else:
            self.prg_identity.set('NCBI/ BLAST+/ tblastx suite' )
            self.current_blast = self.tblastx
        self.current_blast.buildInnerF()
          
    def buildHeader(self, ROW):
        #Put in spaces and identify type of Blast.
        self.makeVSpace(self.inFrm)
        self.makeVSpace(self.inFrm)
        #Left side padding
        tk.Label(self.inFrm, text = '     ').grid(row = ROW, column = 0, rowspan = 1000)
        #Handle to change label when radio button switched
        self.prg_identity = tk.StringVar()
        self.prg_identity.set('NCBI/ BLAST+/ blastn suite' )
        self.prg_label = tk.Label(self.inFrm, textvariable = self.prg_identity, font=('Arial', '10'))
        self.prg_label.grid(row = ROW , column = 1, columnspan=2)
        ROW += 1
        
        #Make Horizontal radio buttons to control switching between program sets.
        self.makeHSpace(self.inFrm, ROW)
        self.radio = tk.IntVar()
        R1 = tk.Radiobutton(self.inFrm, text="blastn", font=('Arial', '12'), variable=self.radio, value=1, command=self.blastSwitch)
        R1.grid(row = ROW, column = 1)
        R2 = tk.Radiobutton(self.inFrm, text="blastp", font=('Arial', '12'), variable=self.radio, value=2, command=self.blastSwitch)
        R2.grid(row = ROW, column = 2)
        R3 = tk.Radiobutton(self.inFrm, text="blastx", font=('Arial', '12'), variable=self.radio, value=3, command=self.blastSwitch)
        R3.grid(row = ROW, column = 3)
        R4 = tk.Radiobutton(self.inFrm, text="tblastn", font=('Arial', '12'), variable=self.radio, value=4, command=self.blastSwitch)
        R4.grid(row = ROW, column = 4)
        R5 = tk.Radiobutton(self.inFrm, text="tblastx", font=('Arial', '12'), variable=self.radio, value=5, command=self.blastSwitch)
        R5.grid(row = ROW, column = 5)
        #Initially toggle blastn as on
        self.radio.set(1)
        ROW += 1
        #Return ROW so blast suite interfaces can be dropped
        return ROW
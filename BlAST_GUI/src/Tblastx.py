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
            #self.ROW needs to be kept track of so code can be moved around and all the griding doesn't need to be adjust
            self.ROW = 0
            #Save a reference to canvas_frame so this class' frame can be destroyed and recreated.
            self.scrFrame = scrFrame
            
            """
            self.inFrm = tk.Frame(scrFrame)
            
            self.buildBlock1()
            
            self.inFrm.grid(row = 0, column =0)
            """
            
    
    
    
    #Functions
    def destroyInnerF(self):
        # Destroy method works but I cannot as of yet get forget to work possibly due to interactive nature of GUI
        self.inFrm.destroy()
    def buildInnerF(self):
        self.inFrm = tk.Frame(self.scrFrame)
        self.buildBlock1()
        self.inFrm.grid(row = 0, column = 0)
    def makeVSpace(self, parent):
        """Makes a vertical blank space in the grid with a label otherwise geometry manager collapses space"""
        tk.Label(parent, text = '').grid(row=self.ROW, column=1)
        self.ROW += 1
    def makeHSpace(self, parent, r, c = 0, width = 5):
        """Make a horizontal blank space which otherwise grid manager collapses."""
        spacer = ' ' * width
        tk.Label(parent, text =  spacer).grid(row = r, column = c)
    def buildBlock2(self):
        '''put in some fake data'''
        for row in range(100):
            tk.Label(self.inFrm, text="%s" % row, width=3, borderwidth="1", 
                     relief="solid").grid(row=self.ROW, column=0)
            t="this is the second column for row %s" %self.ROW
            tk.Label(self.inFrm, text=t).grid(row=self.ROW, column=1)
            self.ROW+=1
    #Widget Layout
    def buildBlock1(self):
        #Put in spaces and identify type of Blast.
        self.makeVSpace(self.inFrm)
        self.makeVSpace(self.inFrm)
        #Left side padding
        tk.Label(self.inFrm, text = '     ').grid(row = self.ROW, column = 0, rowspan = 1000)
        tk.Label(self.inFrm, text='NCBI/ BLAST+/ blastn suite', font=('Arial', '10')).grid(row = self.ROW , column = 1, columnspan=2)
        self.ROW += 1
        
        #Make Horizontal radio buttons to control switching between program sets.
        self.makeHSpace(self.inFrm, self.ROW)
        blastRadio = tk.IntVar()
        R1 = tk.Radiobutton(self.inFrm, text="blastn", font=('Arial', '12'), variable=blastRadio, value=1, command=self.blastSwitch)
        R1.grid(row = self.ROW, column = 1)
        R2 = tk.Radiobutton(self.inFrm, text="blastp", font=('Arial', '12'), variable=blastRadio, value=2, command=self.blastSwitch)
        R2.grid(row = self.ROW, column = 2)
        R3 = tk.Radiobutton(self.inFrm, text="blastx", font=('Arial', '12'), variable=blastRadio, value=3, command=self.blastSwitch)
        R3.grid(row = self.ROW, column = 3)
        R4 = tk.Radiobutton(self.inFrm, text="tblastn", font=('Arial', '12'), variable=blastRadio, value=4, command=self.blastSwitch)
        R4.grid(row = self.ROW, column = 4)
        R5 = tk.Radiobutton(self.inFrm, text="tblastx", font=('Arial', '12'), variable=blastRadio, value=5, command=self.blastSwitch)
        R5.grid(row = self.ROW, column = 5)
        blastRadio.set(1)
        self.ROW += 1
        
        self.makeVSpace(self.inFrm)
        
        tk.Label(self.inFrm, text='Enter Query Sequence', font=('Arial', '14')).grid(row = self.ROW , column = 1, columnspan=4)
        self.ROW += 1
        tk.Label(self.inFrm, text='Enter accession number(s), gi(s), or FASTA sequence(s)', 
                 font=('Arial', '12', 'bold')).grid(row = self.ROW , column = 1, columnspan=4)
        clear_button = tk.Button(self.inFrm, text='Clear', font=('Arial', '9', 'underline'))
        clear_button.grid(row = self.ROW, column =6)
        self.makeHSpace(self.inFrm, self.ROW, 7)
        self.makeHSpace(self.inFrm, self.ROW, 8)
        tk.Label(self.inFrm, text='Query subrange', font=('Arial', '12', 'bold', 'underline')
                 ).grid(row = self.ROW, column = 8, columnspan = 2)
        self.ROW += 1
        # textvariable needs to be assigned to global and clear button linked to it.
        query_box = tk.Text(self.inFrm, font=('Arial', 10), width = 74, height = 5, highlightbackground = 'black', 
                            highlightcolor = 'yellow')
        query_box.grid(row = self.ROW, column = 1, columnspan = 6, rowspan = 5)
        tk.Label(self.inFrm, text = 'From').grid(row = self.ROW, column = 8)
        query_from = tk.Entry(self.inFrm, font=('Arial', 10), width = 8)
        query_from.grid(row = self.ROW, column = 9)
        self.ROW+=1
        tk.Label(self.inFrm, text = 'To').grid(row = self.ROW, column = 8)
        query_to = tk.Entry(self.inFrm, font=('Arial', 10), width = 8)
        query_to.grid(row = self.ROW, column = 9)
        self.ROW+=4
        tk.Label(self.inFrm, text ='Or, upload file', font=('Arial', 12, 'bold')).grid(row = self.ROW, column=1)
        """
        load_query_button = tk.Button(self.inFrm, text='Choose File', command = (lambda : bInputHandler(ioFields)))
        """
        

 









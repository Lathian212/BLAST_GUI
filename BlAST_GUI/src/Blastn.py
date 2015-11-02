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
from tkinter.tix import COLUMN
class Blastn:
    #Attached to radio buttons for switching between Blast types.
    def __init__(self, scrFrame):
        #Globals
        #Save a reference to canvas_frame so this class' frame can be destroyed and recreated.
        self.scrFrame = scrFrame
        #self.ROW needs to be kept track of so code can be moved around and all the griding doesn't need to be adjusted
        self.ROW = 0
        #Below tkinter boolean keeps track of align two or more sequences checkbutton, initializes to false.
        self.checkBut = tk.BooleanVar() 
            
    
    
    
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
        #For aligning two or more sequences an entire block as to be added to the display
        if self.checkBut.get():
            self.buildBlock2()
        #In scrFrame I have two frames one from radio buttons at row = 0, column =0 and this one at row = 1, column =0
        self.inFrm.grid(row = 1, column = 0)
    def makeVSpace(self, parent):
        """Makes a vertical blank space in the grid with a label otherwise geometry manager collapses space"""
        tk.Label(parent, text = '').grid(row=self.ROW, column=1)
        self.ROW += 1
    def makeHSpace(self, parent, r, c = 0, width = 5):
        """Make a horizontal blank space which otherwise grid manager collapses."""
        spacer = ' ' * width
        tk.Label(parent, text =  spacer).grid(row = r, column = c)
    def loadHandler(self):
        """Handles load file button putting selected file into -query"""
        pass
    def saveHandler(self):
        """Handles save file button putting selected file into -out"""
        pass
    def buildBlock2(self):
        #This is a lot of duplicate code perhaps a method could construct it.
        self.makeVSpace(self.inFrm)
        #Left side padding (calculated rowspan by printing out self.ROW at end of this block)
        tk.Label(self.inFrm, text = '     ').grid(row = self.ROW, column = 0, rowspan = 15)
        
        tk.Label(self.inFrm, text='Enter Subject Sequence:', font=('Arial', '14', 'underline')).grid(row = self.ROW , column = 1, 
                                                                                                    columnspan=4, sticky = 'w')
        self.ROW += 1
        tk.Label(self.inFrm, text='Enter accession number(s), gi(s), or FASTA sequence(s)', 
                 font=('Arial', '12', 'bold')).grid(row = self.ROW , column = 1, columnspan=4, sticky ='w')
        clear_button = tk.Button(self.inFrm, text='Clear', font=('Arial', '9', 'underline'))
        clear_button.grid(row = self.ROW, column =4)
        tk.Label(self.inFrm, text='Subject subrange', font=('Arial', '12', 'bold', 'underline')
                 ).grid(row = self.ROW, column = 5, columnspan = 4, sticky = 'w')
        self.ROW += 1
        # textvariable needs to be assigned to global and clear button linked to it.
        # Also it needs to be scrollable in case the user puts a lot into it
        query_box = tk.Text(self.inFrm, font=('Arial', 10), width = 74, height = 5, highlightbackground = 'black', 
                            highlightcolor = 'yellow')
        query_box.grid(row = self.ROW, column = 1, columnspan = 6, rowspan = 5, sticky = 'w')
        tk.Label(self.inFrm, text = 'From').grid(row = self.ROW, column = 8)
        query_from = tk.Entry(self.inFrm, font=('Arial', 10), width = 8)
        query_from.grid(row = self.ROW, column = 9)
        self.ROW+=1
        tk.Label(self.inFrm, text = 'To').grid(row = self.ROW, column = 8)
        query_to = tk.Entry(self.inFrm, font=('Arial', 10), width = 8)
        query_to.grid(row = self.ROW, column = 9)
        self.ROW+=4
        tk.Label(self.inFrm, text ='Or, upload file', font=('Arial', 12, 'bold')).grid(row = self.ROW, column=1, sticky = 'E')
        load_query_button = tk.Button(self.inFrm, text='Choose File', command = (lambda : self.loadHandler()))
        load_query_button.grid(row = self.ROW, column = 2)
        load_status = tk.Label(self.inFrm, text='No file chosen', font=('Arial', '10'))
        load_status.grid(row = self.ROW , column = 3)
        self.ROW+=1
    def align2OrMore(self):
        """Destroys existing layout and then calls buildBlock method to either put in or take out extra box for
        aligning two or more sequences locally"""
        self.destroyInnerF()
        self.buildInnerF()
    #Widget Layout
    def buildBlock1(self):        
        self.makeVSpace(self.inFrm)
        #Left side padding (calculated rowspan by printing out self.ROW at end of this block)
        tk.Label(self.inFrm, text = '     ').grid(row = self.ROW, column = 0, rowspan = 15)
        
        tk.Label(self.inFrm, text='Enter Query Sequence:', font=('Arial', '14', 'underline')).grid(row = self.ROW , column = 1, 
                                                                                                    columnspan=4, sticky = 'w')
        self.ROW += 1
        tk.Label(self.inFrm, text='Enter accession number(s), gi(s), or FASTA sequence(s)', 
                 font=('Arial', '12', 'bold')).grid(row = self.ROW , column = 1, columnspan=4, sticky ='w')
        clear_button = tk.Button(self.inFrm, text='Clear', font=('Arial', '9', 'underline'))
        clear_button.grid(row = self.ROW, column =4)
        tk.Label(self.inFrm, text='Query subrange', font=('Arial', '12', 'bold', 'underline')
                 ).grid(row = self.ROW, column = 5, columnspan = 4, sticky = 'w')
        self.ROW += 1
        # textvariable needs to be assigned to global and clear button linked to it.
        # Also it needs to be scrollable in case the user puts a lot into it
        query_box = tk.Text(self.inFrm, font=('Arial', 10), width = 74, height = 5, highlightbackground = 'black', 
                            highlightcolor = 'yellow')
        query_box.grid(row = self.ROW, column = 1, columnspan = 6, rowspan = 5, sticky = 'w')
        tk.Label(self.inFrm, text = 'From').grid(row = self.ROW, column = 8)
        query_from = tk.Entry(self.inFrm, font=('Arial', 10), width = 8)
        query_from.grid(row = self.ROW, column = 9)
        self.ROW+=1
        tk.Label(self.inFrm, text = 'To').grid(row = self.ROW, column = 8)
        query_to = tk.Entry(self.inFrm, font=('Arial', 10), width = 8)
        query_to.grid(row = self.ROW, column = 9)
        self.ROW+=4
        tk.Label(self.inFrm, text ='Or, upload file', font=('Arial', 12, 'bold')).grid(row = self.ROW, column=1, sticky = 'E')
        load_query_button = tk.Button(self.inFrm, text='Choose File', command = (lambda : self.loadHandler()))
        load_query_button.grid(row = self.ROW, column = 2)
        load_status = tk.Label(self.inFrm, text='No file chosen', font=('Arial', '10'))
        load_status.grid(row = self.ROW , column = 3)
        self.ROW+=1
        tk.Label(self.inFrm, text ='Pick save file and format', font=('Arial', 12, 'bold')).grid(row = self.ROW, 
                                                                                                 column=1, sticky = 'E')
        save_query_button = tk.Button(self.inFrm, text='Choose File', command = (lambda : self.saveHandler()))
        save_query_button.grid(row = self.ROW, column = 2)
        save_status = tk.Label(self.inFrm, text='No file chosen', font=('Arial', '10'))
        save_status.grid(row = self.ROW , column = 3)
        #Replace below with drop down list once learn place geometry manager
        save_output_button = tk.Button(self.inFrm, text='Choose Output')
        save_output_button.grid(row = self.ROW, column = 4)
        self.ROW+=1
        tk.Label(self.inFrm, text ='Job Title', font=('Arial', 12, 'bold')).grid(row = self.ROW, column=1, sticky = 'E')
        job_title = tk.Entry(self.inFrm, font=('Arial', 10))
        job_title.grid(row = self.ROW, column = 2, columnspan = 8)
        job_title.configure(width=80)
        self.ROW+=1
        self.makeVSpace(self.inFrm)
        check_button = tk.Checkbutton(self.inFrm, text = 'Align two or more sequences', font=('Arial', 12, 'bold'),
                                      variable = self.checkBut, command = self.align2OrMore)
        check_button.grid(row = self.ROW, column = 1)
        self.ROW+=1
        
        
        

 









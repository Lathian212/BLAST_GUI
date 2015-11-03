'''
Created on Oct 10, 2015
Going to try to get place manager to work with DropDownList
@author: Lathian
'''
from tkinter import *
import os


class DropDownList(Frame):
    def __init__(self, dropList, variables, field, *args, **kwargs):
        self.dropList = dropList
        self.kwargs = kwargs
        # Listbox length
        if 'listboxLength' in kwargs:
            self.listboxLength = kwargs['listboxLength']
            #Otherwise Frame constructor balks if this isn't removed.
            del kwargs['listboxLength']
        else:
            self.listboxLength = 8
        #Parent constructor must be explicitly called else error.
        Frame.__init__(self, *args, **kwargs)
        self.makeLabel()
        self.makeButton()
        
    def makeListBox(self):
        self.listboxUp = False
        self.listbox = Listbox(self)
        self.listbox.config(selectmode = 'single')
        self.listbox.bind("<Double-1>", self.selection)
        self.listbox.bind("<Return>", self.selection)
        #Populate list box.
        for choice in self.dropList:
            self.listbox.insert(END,choice)
        self.listbox.grid(row = 0, column = 0)
    def selection(self, Event):
        #Problem with just highlighting a list selection not engough to activate it so this:
        index = self.listbox.curselection()
        self.listbox.activate(index)
        self.var.set(self.listbox.get(ACTIVE))
        variables.append([field, self.var.get()])
        print(variables)
        self.listbox.destroy()
    def b_Handler(self): 
        self.makeListBox()  
        # Set up label: 
    def makeLabel(self):
        self.label = Label(self)
        # Can pass in 'textvariable' : 'StrigVar()value' in **kwargs to get a handle on text in Label widget or will
        # create this variable so can be accessed from outside class.
        if 'textvariable' in self.kwargs:
            # var is just a made up variable whose scope is this Frame derived class 
            self.var = self.label['textvariable']= self.kwargs['textvariable']
        else :
            self.var = self.label["textvariable"] = StringVar()
        # Find maximum width of text needing to be displayed in drop down when inserted into label.
        self.labelSize = len(max(dropList, key = len)) + 5 
        # Set default text to first element in list but pad with spaces for max size in list.
        self.defaultText = dropList[0] + (' ' * (self.labelSize - len(dropList[0])))
        self.var.set(self.defaultText)
        
        #Note to self:"cannot have grid and place geometry manager fix this so can use place with drop down menu.
        self.label.grid(row =0, column =0)
    def makeButton(self):
        # Setting up button. It will be linked to whether Listbox is up or not.
        self.button = Button(self)
        os.chdir('../resources/')
        self.photo = PhotoImage(file='NCBI_Button.gif')
        self.button.config(image = self.photo, width ='10', height = '10')
        self.button.config(command = self.b_Handler)
        
        #Note to self:"cannot have grid and place geometry manager fix this so can use place with drop down menu.
        self.button.grid(row =0, column = 1, sticky = N)
    
    

if __name__ == '__main__':
    dropList = [ 'Dora Lyons (7714)', 'Hannah Golden (6010)', 'Walker Burns (9390)', 'Dieter Pearson (6347)', 'Allen Sullivan (9781)', 'Warren Sullivan (3094)', 'Genevieve Mayo (8427)', 'Igor Conner (4740)', 'Ulysses Shepherd (8116)', 'Imogene Bullock (6736)', 'Dominique Sanchez (949)', 'Sean Robinson (3784)', 'Diana Greer (2385)', 'Arsenio Conrad (2891)', 'Sophia Rowland (5713)', 'Garrett Lindsay (5760)', 'Lacy Henry (4350)', 'Tanek Conley (9054)', 'Octavia Michael (5040)', 'Kimberly Chan (1989)', 'Melodie Wooten (7753)', 'Winter Beard (3896)', 'Callum Schultz (7762)', 'Prescott Silva (3736)', 'Adena Crane (6684)', 'Ocean Schroeder (2354)', 'Aspen Blevins (8588)', 'Allegra Gould (7323)', 'Penelope Aguirre (7639)', 'Deanna Norman (1963)', 'Herman Mcintosh (1776)', 'August Hansen (547)', 'Oscar Sanford (2333)', 'Guy Vincent (1656)', 'Indigo Frye (3236)', 'Angelica Vargas (1697)', 'Bevis Blair (4354)', 'Trevor Wilkinson (7067)', 'Kameko Lloyd (2660)', 'Giselle Gaines (9103)', 'Phyllis Bowers (6661)', 'Patrick Rowe (2615)', 'Cheyenne Manning (1743)', 'Jolie Carney (6741)', 'Joel Faulkner (6224)', 'Anika Bennett (9298)', 'Clayton Cherry (3687)', 'Shellie Stevenson (6100)', 'Marah Odonnell (3115)', 'Quintessa Wallace (5241)', 'Jayme Ramsey (8337)', 'Kyle Collier (8284)', 'Jameson Doyle (9258)', 'Rigel Blake (2124)', 'Joan Smith (3633)', 'Autumn Osborne (5180)', 'Renee Randolph (3100)', 'Fallon England (6976)', 'Fallon Jefferson (6807)', 'Kevyn Koch (9429)', 'Paki Mckay (504)', 'Connor Pitts (1966)', 'Rebecca Coffey (4975)', 'Jordan Morrow (1772)', 'Teegan Snider (5808)', 'Tatyana Cunningham (7691)', 'Owen Holloway (6814)', 'Desiree Delaney (272)', 'Armand Snider (8511)', 'Wallace Molina (4302)', 'Amela Walker (1637)', 'Denton Tillman (201)', 'Bruno Acevedo (7684)', 'Slade Hebert (5945)', 'Elmo Watkins (9282)', 'Oleg Copeland (8013)', 'Vladimir Taylor (3846)', 'Sierra Coffey (7052)', 'Holmes Scott (8907)', 'Evelyn Charles (8528)', 'Steel Cooke (5173)', 'Roth Barrett (7977)', 'Justina Slater (3865)', 'Mara Andrews (3113)', 'Ulla Skinner (9342)', 'Reece Lawrence (6074)', 'Violet Clay (6516)', 'Ainsley Mcintyre (6610)', 'Chanda Pugh (9853)', 'Brody Rosales (2662)', 'Serena Rivas (7156)', 'Henry Lang (4439)', 'Clark Olson (636)', 'Tashya Cotton (5795)', 'Kim Matthews (2774)', 'Leilani Good (5360)', 'Deirdre Lindsey (5829)', 'Macy Fields (268)', 'Daniel Parrish (1166)', 'Talon Winters (8469)' ]
    
    root = Tk()
    variables = []
    field = 'names'
    dropDown = DropDownList(dropList, variables, field)
    dropDown.grid(row=0, column=0)  
      
    root.mainloop()
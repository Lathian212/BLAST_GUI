'''

This should be main that's stripped of the functions and master frames
containing all the Widget's

Right now it's a mess.

@author: Lathian
'''
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from Autocomplete import AutocompleteEntry
import os
import cmd
# Find way to get PATH so platform independent
cmd = '/usr/local/ncbi/blast/bin/'
# Options dictionary needs to be expanded and possibly tailored for each type of blast.
gridRow = 0
ioFields = []
fields = ['db', 'entrez_query', 'evalue', 'outfmt']
def mHandler(str, cmdS, Menubutton):
    # print(str)
    # Changing immutable string so need to declare it global so interpreter knows what I refer to
    global cmd
    mbutton.config(text=str)
    cmdS += str
    cmd = cmdS 
    print(cmdS)
def bInputHandler(ioFields):
    filename = askopenfilename()
    filename = ' -query ' + filename
    ioFields.append(filename)
    print(ioFields)
    # listing = os.popen('cat ' + filename).readlines()
    # print(listing)
def bOutputHandler(ioFields):
    savefilename = asksaveasfilename()
    savefilename = ' -out ' + savefilename
    ioFields.append(savefilename)
    print(ioFields)

def systemCall(cmd, ioFields, vars):
    commandString = cmd
    for file in ioFields:
        commandString += file
    for ( fieldLabel, value) in vars:
        commandString += ' -' + fieldLabel+ ' ' + value.get()
    commandString += ' -remote'
    print(commandString)
    # os.system(commandString)
    print('Done')

def makeform(mainFrame, fields, gridRow):
    form = Frame(mainFrame)                              # make outer frame
    left = Frame(form)                              # make two columns
    rite = Frame(form)
    form.grid(row = (gridRow), column = 0)
    gridRow+=1; 
    left.pack(side=LEFT)
    rite.pack(side=RIGHT, expand=YES, fill=X)       # grow horizontal

    variables = []
    for field in fields:
        lab = Label(left, width=10, text=field)      # add to columns
        ent = Entry(rite)
        lab.pack(side=TOP)
        ent.pack(side=TOP, fill=X)                  # grow horizontal
        var = StringVar()
        ent.config(textvariable=var)                # link field to var
        var.set('enter here')
        variables.append([field, var])
    return variables
    

root = Tk()
root.title('GUI for NCBI Blast+')
# print(root.keys())
mainFrame = Frame(root)
mainFrame.grid(row = 0, column =0)

label1 = Label(mainFrame, text = 'Click Button To Select Blast Type: ')
label1.grid(row = 0, column =0)

mbutton = Menubutton(mainFrame, text='******')     # the pull-down stands alone
picks   = Menu(mbutton)
mbutton.config(menu=picks)
picks.add_command(label='Blastn',  command=(lambda : mHandler('Blastn',cmd, mbutton)))
picks.add_command(label='blastp',  command=(lambda : mHandler('blastp', cmd, mbutton)))
picks.add_command(label='blastx', command=(lambda  : mHandler('blastx', cmd, mbutton)))
picks.add_command(label='tblastn', command=(lambda : mHandler('tblastn', cmd, mbutton)))
picks.add_command(label='tblastx', command=(lambda : mHandler('tblastx', cmd, mbutton)))
mbutton.grid(row =0 , column =1)
mbutton.config(bg='white', bd=4, relief=RAISED)

label0 = Label(mainFrame, text='')
label0.grid(row =1 , column= 0)
label2 = Label(mainFrame, text = 'Click Button To Select Input File: ')
label2.grid(row =2, column =0)
button1 = Button(mainFrame, text='INPUT', command = (lambda : bInputHandler(ioFields)))
button1.grid(row = 2, column =1)

button2 = Button(mainFrame, text='OUTPUT', command = (lambda : bOutputHandler(ioFields)))
button2.grid(row = 3, column = 1)

gridRow =4
vars = makeform(root, fields, gridRow)
gridRow += len(vars)

""" Code to make autocomplete entry box"""
autocompleteList = [ 'Dora Lyons (7714)', 'Hannah Golden (6010)', 'Walker Burns (9390)', 'Dieter Pearson (6347)', 'Allen Sullivan (9781)', 'Warren Sullivan (3094)', 'Genevieve Mayo (8427)', 'Igor Conner (4740)', 'Ulysses Shepherd (8116)', 'Imogene Bullock (6736)', 'Dominique Sanchez (949)', 'Sean Robinson (3784)', 'Diana Greer (2385)', 'Arsenio Conrad (2891)', 'Sophia Rowland (5713)', 'Garrett Lindsay (5760)', 'Lacy Henry (4350)', 'Tanek Conley (9054)', 'Octavia Michael (5040)', 'Kimberly Chan (1989)', 'Melodie Wooten (7753)', 'Winter Beard (3896)', 'Callum Schultz (7762)', 'Prescott Silva (3736)', 'Adena Crane (6684)', 'Ocean Schroeder (2354)', 'Aspen Blevins (8588)', 'Allegra Gould (7323)', 'Penelope Aguirre (7639)', 'Deanna Norman (1963)', 'Herman Mcintosh (1776)', 'August Hansen (547)', 'Oscar Sanford (2333)', 'Guy Vincent (1656)', 'Indigo Frye (3236)', 'Angelica Vargas (1697)', 'Bevis Blair (4354)', 'Trevor Wilkinson (7067)', 'Kameko Lloyd (2660)', 'Giselle Gaines (9103)', 'Phyllis Bowers (6661)', 'Patrick Rowe (2615)', 'Cheyenne Manning (1743)', 'Jolie Carney (6741)', 'Joel Faulkner (6224)', 'Anika Bennett (9298)', 'Clayton Cherry (3687)', 'Shellie Stevenson (6100)', 'Marah Odonnell (3115)', 'Quintessa Wallace (5241)', 'Jayme Ramsey (8337)', 'Kyle Collier (8284)', 'Jameson Doyle (9258)', 'Rigel Blake (2124)', 'Joan Smith (3633)', 'Autumn Osborne (5180)', 'Renee Randolph (3100)', 'Fallon England (6976)', 'Fallon Jefferson (6807)', 'Kevyn Koch (9429)', 'Paki Mckay (504)', 'Connor Pitts (1966)', 'Rebecca Coffey (4975)', 'Jordan Morrow (1772)', 'Teegan Snider (5808)', 'Tatyana Cunningham (7691)', 'Owen Holloway (6814)', 'Desiree Delaney (272)', 'Armand Snider (8511)', 'Wallace Molina (4302)', 'Amela Walker (1637)', 'Denton Tillman (201)', 'Bruno Acevedo (7684)', 'Slade Hebert (5945)', 'Elmo Watkins (9282)', 'Oleg Copeland (8013)', 'Vladimir Taylor (3846)', 'Sierra Coffey (7052)', 'Holmes Scott (8907)', 'Evelyn Charles (8528)', 'Steel Cooke (5173)', 'Roth Barrett (7977)', 'Justina Slater (3865)', 'Mara Andrews (3113)', 'Ulla Skinner (9342)', 'Reece Lawrence (6074)', 'Violet Clay (6516)', 'Ainsley Mcintyre (6610)', 'Chanda Pugh (9853)', 'Brody Rosales (2662)', 'Serena Rivas (7156)', 'Henry Lang (4439)', 'Clark Olson (636)', 'Tashya Cotton (5795)', 'Kim Matthews (2774)', 'Leilani Good (5360)', 'Deirdre Lindsey (5829)', 'Macy Fields (268)', 'Daniel Parrish (1166)', 'Talon Winters (8469)' ]
    # For regular expression pattern search.
def matches(fieldValue, acListEntry):
    pattern = re.compile(re.escape(fieldValue) + '.*', re.IGNORECASE)
    return re.match(pattern, acListEntry)
autoEntry = AutocompleteEntry(autocompleteList, root, listboxLength=6, width=32, matchesFunction=matches)
# Below StringVar associated with entry box.
autoEntryVar = autoEntry.var
vars.append(['Organism', autoEntryVar])
autoEntry.grid(row = gridRow, column = 0, sticky = W)
gridRow += 1

blastButton = Button(root, text='BLAST', command=(lambda: systemCall(cmd, ioFields, vars)))
blastButton.grid(row = gridRow, column = 0)








root.mainloop()


"""
if __name__ == '__main__':
    root = Tk()
    vars = makeform(root, fields)
    Button(root, text='Fetch', command=(lambda: fetch(vars))).pack(side=LEFT)
    Quitter(root).pack(side=RIGHT)
    root.bind('<Return>', (lambda event: fetch(vars)))
    root.mainloop()
"""
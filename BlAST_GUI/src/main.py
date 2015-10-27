'''
Created on Oct 27, 2015

@author: Lathian
This is the top level file. The main control logic should be here.

'''

"""Pop up a Tk root window and make Scrollable Canvas it's child"""
import ScrollableCanvas as sc
import Blastn as bn
import tkinter as tk


root = tk.Tk()
root.title('GUI for NCBI Blast+')
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
sCanvas = sc.ScrollableCanvas(root)
sFrame = sCanvas.getScrFrame()
blastn = bn.Blastn(sFrame)
"""
input('Hit enter to forget inner frame')
blastn.forgetInnerF()
"""
root.mainloop() 


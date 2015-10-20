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

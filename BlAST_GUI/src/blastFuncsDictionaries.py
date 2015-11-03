'''
Created on Nov 3, 2015
I will create make functions for each of the 5 dictionaries necessary to store the tk.StringVar()'s for all the options
associated with each command line tool. These dictionaries are the 'wiring' hooking up each widget so that when the BLAST
button is pressed all the information on the page can be collected and sent to subprocess. Also, these dictionaries will allow
state information to be saved when flipping between the blast suite pages.

Supplemental list's, dictionaries and functions will also be here.
@author: Lathian
'''

#The index of this list is the number that needs to be passed to the command line
blastn_outputfmt = ['pairwise'  , 'query-anchored showing identities'  , 'query-anchored no identities'  , 
                    'flat query-anchored, show identities'  , 'flat query-anchored, no identities'  , 'XML Blast output'  , 
                    'tabular'  , 'tabular with comment lines'  , 'Text ASN.1'  , 'Binary ASN.1'  , 'Comma-separated values'  , 
                    'BLAST archive format (ASN.1)'  , 'JSON Seqalign output'  , 'JSON Blast output'  , 'XML2 Blast output']
""" Just checking I did my regex correctly 
for i, val in enumerate(blastn_outputfmt):
    print(str(i) +'  '+val)
"""
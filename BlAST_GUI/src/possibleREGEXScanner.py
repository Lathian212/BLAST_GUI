'''
Created on Oct 9, 2015

@author: Lathian
http://stackoverflow.com/questions/10477294/how-do-i-search-for-a-pattern-within-a-text-file-using-python-combining-regex
'''


import re
import os



os.chdir(os.getcwd()+'/taxonomy')

print(os.getcwd())
"""
linesList = []

linesList = open('names.dmp', 'r').readlines()

for line in linesList:
    print(line)
"""

pattern = re.compile("[^a-zA-z0-9]pro", re.IGNORECASE)
for i, line in enumerate(open('names.dmp')):
    for match in re.finditer(pattern, line):
        print ('Found on line %s: %s' % (i+1, match.groups()) + line)

""" for row_number, row in enumerate(cursor):
The enumerate() function adds a counter to an iterable.

So for each element in cursor, a tuple is produced with (counter, element); 
the for loop binds that to row_number and row, respectively. """
#!/usr/bin/env python3
#text2files.py
#usage:   python3 text2folders.py <textfile>
import os
import sys

#get filename from command line argument
filename = sys.argv[1]
f= open(filename, 'r')

#loop through each line in a textfile and make a new directory using that name
for i in f:
    i = i.strip()
    if not os.path.exists(i):
        os.mkdir(i)
        print ("Created folder", i)
    else :
        print("Folder", i, "already exists... moving on.")
f.close()
print ("Complete")

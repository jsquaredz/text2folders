#!/usr/bin/env python3
#text2files.py
#usage:   python3 text2folders.py <textfile>
import os
import sys

def makefolders(filename):
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

#get filename from command line argument
try:
    filename = sys.argv[1]
    makefolders(filename)
    
except:
    print ("You must add the filename of the text file as a command line argument (e.g. python3 text2folders.py <filename.txt>)")

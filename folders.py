import os
import sys

filename = sys.argv[1]
f= open(filename, 'r')


for i in f:
    i = i.strip()
    os.mkdir(i)


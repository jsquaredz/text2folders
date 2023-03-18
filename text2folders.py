#!/usr/bin/env python3
import os
import sys

def make_folders_from_text_file(file_path):
    """
    Reads a text file line by line and creates a folder with the name of each line if it doesn't already exist.
    :param file_path: The path of the text file.
    """
    with open(file_path) as f:
        for line in f:
            folder_name = line.strip()
            if not os.path.exists(folder_name):
                os.mkdir(folder_name)
                print(f"Created folder {folder_name}")
            else:
                print(f"Folder {folder_name} already exists, skipping.")
    print("Complete")

# Get the filename from command line arguments.
if len(sys.argv) == 2:
    file_path = sys.argv[1]
    make_folders_from_text_file(file_path)
else:
    print("Please specify a text file as a command line argument, e.g. 'python3 text2folders.py filename.txt'")

"""List Dir. 

Sample Code to list sub-dirs and files in a given folder
"""
import os

subdirs = []
files = []

for entry in os.scandir('/var/log'):
    if entry.is_dir():
        subdirs.append(entry.path)
    elif entry.is_file():
        files.append(entry.path)

print('Sub Dirs:')
print(subdirs)

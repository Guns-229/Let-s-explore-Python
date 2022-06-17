# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 06:19:01 2017

@author: johri_m
"""

import os
import subprocess
import shutil
from optparse import OptionParser


htmlFiles = []
parser = OptionParser()
parser.add_option("-s", "--source", dest="source",
                  help="parent source directory", metavar="source")
parser.add_option("-d", "--dest", dest="dest",
                  help="destination directory")

(options, args) = parser.parse_args()
print(options)

for d in os.walk(options.source):
    for f in d[2]:
        if os.path.splitext(f)[1].lower() in ['.jpg', '.jpeg', '.png', '.gif']:
            print("Processing: ", f)
            htmlFiles.append(os.path.abspath(os.path.join(d[0], f)))

cwd = os.getcwd()
dest = options.dest
print("options.dest" + dest)
for f in htmlFiles:
    print("Copying file:", f)
    d = os.path.split(f.split(cwd)[1])[0][1:]
    dest_path = os.path.join(dest, d)
    print("path", dest_path)
    os.makedirs(dest_path, exist_ok=True)
    shutil.copy(f, dest_path)

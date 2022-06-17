# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 08:50:42 2016

@author: mayankjohri@gmail.com
"""
import traceback

# Try to get a file name
try:
#     fn = input('File Name (temp.txt): ').strip()
    fn = "temp.txt"
    # Numbering lines
    for i, s in enumerate(open(fn)):
        print( i + 1,"> ", s,)
        if i == 2:
            raise ValueError

# If an error happens
except:
    # And save it on a file 
    with open("trace_asd.log", "a") as file:
        traceback.print_exc(file=file)

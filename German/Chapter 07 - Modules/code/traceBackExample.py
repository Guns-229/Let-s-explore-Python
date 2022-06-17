# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 08:50:42 2016

@author: hclqaVirtualBox1
"""


import traceback

# Try to get a file name
try:
    fn = input('File Name (temp.txt): ').strip()

    # Numbering lines
    for i, s in enumerate(open(fn)):
        print( i + 1,"> ", s,)

# If an error happens
except:

    # Show it on the screen
    trace = traceback.format_exc()

    # And save it on a file
    print ('An error happened:\n', trace)
 
    with open("trace_asd.log", "a+") as file:
        file.write(trace)
    
#    file('trace_asd.log', 'a').write(trace)

    # end the program
    raise SystemExit
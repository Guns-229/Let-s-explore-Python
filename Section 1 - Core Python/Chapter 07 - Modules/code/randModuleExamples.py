# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 07:20:44 2016

@author: hclqaVirtualBox1
"""
#
#import random
#
#print(random.randrange(10, 133))
#
#import math
#
##import cmath
#
#
#print(math.factorial(10))
## Complex
#for cpx in [3j, 1.5 + 1j, -2 - 2j]:
#
#    # Polar coordinate conversion
#    plr = cmath.polar(cpx)
#    print ('Complex:', cpx)
#    print ('Polar:', plr, '(in radians)')
#    print ('Amplitude:', abs(cpx))
#    print ('Angle:', math.degrees(plr[1]), '(grades)')
import os
#
#print(os.path.basename(r"C:\Users\hclqaVirtualBox1\Desktop\Python Training\tutorial\temp.txt"))
#print(os.path.abspath(".."))

fileNameWin = r"log\testing.txt"
dirNameWin ='C:\\temp\\test\\'
fileName = "log/testing.txt"
dirName = "/Users/MJ/test/"
# BAD Idea
print(dirName + "\\" +fileName)
# 
print(os.path.join(dirName, fileName))

rl = os.path.relpath(r"C:\Users\hclqaVirtualBox1\Desktop\Python Training\tutorial\modules sample\pacOne\modOne.py")

print(rl)
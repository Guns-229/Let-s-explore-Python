# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 07:47:17 2017

@author: johri_m
"""

#question = [
#        ["What is the diameter of earth", "1000", "112", "23232"],
#        ["where is clarke's ring", "inside sun", "around earth"],
#        "what is xyz", "abc", "asd"],
#        ""
#        ]

correct = 0
wrong = 0
x = input("What is the daimeter of earth")
if(x == str(1000)):
    correct +=1
else:
    wrong +=1
    
x = input("Where is clarks ring")
if(x == "around earth"):
    correct +=1
else:
    wrong +=1
    
print("Correct count: ", correct)
print("wrong count: ", wrong)

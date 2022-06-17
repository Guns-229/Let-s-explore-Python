# -*- coding: utf-8 -*-
"""
Guess the password 

Simple program to demostrate the use of while statement
"""
#x=int(input('Enter a passkeyid: '))
#print(type(x))
#while x != 10:
#    print(x),
#    x=int(input('Enter a passkeyid: '))
#key=input("Press key...")
#
#
#x=input('Enter a passkeyid: ')
#print(type(x))
#while x != str(10):
#    print(x),
#    x=input('Enter a passkeyid: ')
#key=input("Press key...")
"""
Bad Code
"""
print("bad code")
x=input('Enter a passkeyid: ')
print(type(x))
while x != "abc":
    print(x),
    x=input('Enter a passkeyid: ')
key=input("Press key...")

"""
Better code
"""
print("Better code")
while x != "abc":
    x=input('Enter a passkeyid: ')
    print(x),
key=input("Press key...")

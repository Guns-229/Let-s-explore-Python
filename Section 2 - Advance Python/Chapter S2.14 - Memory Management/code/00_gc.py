#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 12:19:48 2018

@author: mayank
"""
import gc
import pprint


def test(t=[]):
    t.append(t)
    print(t)


for _ in range(100):
    test()

print('Collecting...')
n = gc.collect()
print('Unreachable objects:', n)
print('Remaining Garbage:',)
pprint.pprint(gc.garbage)

# Break the cycle
print
print('Breaking the cycle')
#gc.garbage.set_next(None)
print('Removing references in gc.garbage')
del gc.garbage[:]

# Now the objects are removed
print
print('Collecting...')
n = gc.collect()
print('Unreachable objects:', n)
print('Remaining Garbage:',)
pprint.pprint(gc.garbage)

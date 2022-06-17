#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 12:19:48 2018

@author: mayank
"""
import gc
import pprint


def test():
    if "t" not in locals():
        t = []
    t.append(t)


for _ in range(6000):
    test()
    if _ % 100 == 0:
        print("Cleaning requested")
#        gc.collect()
    print(gc.get_count())
    print(gc.get_stats())
    pprint.pprint(gc.garbage)

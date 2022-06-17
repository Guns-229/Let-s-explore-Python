#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 12:19:48 2018

@author: mayank
"""
import gc


def test():
    if "t" not in locals():
        t = []
    t.append(t)


#gc.set_debug(gc.DEBUG_LEAK)
gc.set_threshold(50, 10, 10)
for _ in range(100):
    test()
    if _ % 20 == 0:
        print("Cleaning requested")
        gc.collect()
        del gc.garbage[:]
    print(gc.get_count())
    print(gc.get_stats())

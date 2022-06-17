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


for _ in range(1000):
    test()
    print(gc.get_count())
    print(gc.get_stats())

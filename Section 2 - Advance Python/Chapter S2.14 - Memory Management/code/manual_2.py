#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 13:48:00 2018

@author: mayank
"""
import sys
import gc


def make_cycle():
    llst = {}
    llst[0] = llst


def main():
    collected = gc.collect()
    print("collected {0} objects.".format(collected))
    print("Creating cycles...")
    for i in range(1111):
        make_cycle()
    collected = gc.collect()
    print("collected %d objects." % (collected))


if __name__ == "__main__":
    print(gc.isenabled())
    gc.disable()
    print(gc.isenabled())
    ret_val = main()
    print(ret_val)
    sys.exit(ret_val)

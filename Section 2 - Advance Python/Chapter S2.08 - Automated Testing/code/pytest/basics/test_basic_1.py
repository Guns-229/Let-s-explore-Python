# -*- coding: utf-8 -*-
"""
Created on Fri May 12 04:16:14 2017.

@author: johri_m.
"""


def increment(x):
    """."""
    return x + 1


def test_will_fail():
    """."""
    print("testing 3+1")
    assert increment(3) == 5


def test_will_pass():
    """."""
    assert increment(4) == 5

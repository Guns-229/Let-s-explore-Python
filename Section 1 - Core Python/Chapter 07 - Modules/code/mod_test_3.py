# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 08:24:08 2016

@author: hclqaVirtualBox1
"""


def test1():
    """."""
    print("TEST")
    from modOne import test
    test()


def test2():
    """."""
    from modTwo import test
    test()


def test3():
    """."""
    print("TEST 3")
    from modOne import test
    test()

test1()
test2()
test1()
test3()
test()

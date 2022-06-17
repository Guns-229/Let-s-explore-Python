# -*- coding: utf-8 -*-
"""
Created on Fri May 12 04:48:04 2017.

@author: johri_m
"""
import traceback
from sample_script import multiple


def gfn():
    """."""
    return traceback.extract_stack(None, 2)[0][2]

# def setup_function(function):
#     print(gfn(),  function.__name__)
#
# def teardown_function(function):
#     print(gfn(),  function.__name__)
#
# def test_numbers_3_4():
#     print(gfn())
#     assert add(3, 4) == 7
#
# def test_strings_a_3():
#     print(gfn())
#     assert multiple('a', 3) == 'aaa'


class TestClass:

    def setup(self):
        print(gfn(), "MMM")

    def teardown(self):
        print(gfn(), "NNN")

    def setup_class(cls):
        print("%s       class:%s" % (gfn(), cls.__name__))

    def teardown_class(cls):
        print("teardown_class    class:%s" % cls.__name__)

    def setup_method(self, method):
        print("setup_method      method:%s" % method.__name__)

    def teardown_method(self, method):
        print("teardown_method   method:%s" % method.__name__)

    def test_numbers_5_6(self):
        print("test_numbers_5_6")
        assert multiple(5, 6) == 30

    def test_strings_b_2(self):
        print("test_strings_b_2")
        assert multiple('b', 2) == 'bb'

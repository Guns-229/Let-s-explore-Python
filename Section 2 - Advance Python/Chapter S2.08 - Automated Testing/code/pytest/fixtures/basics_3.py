# -*- coding: utf-8 -*-
"""
Created on Fri May 12 04:48:04 2017

Setting fixture to an entire test file is to set the `pytestmark` variable

NOTE: 
    By doing this, we set the fixtures globally for this file and 
    all test functions within it will use these fixtures. One thing 
    to note is that all your functions may not need this fixture. 
    If that's the case, it's better to directly specify each fixture 
    for a test function rather than taking the lazy road and marking 
    them all at the top. With larger fixtures, this can cause the tests 
    to load slower as the fixtures are built.

@author: johri_m
"""
import pytest
import traceback

def gfn():
    return traceback.extract_stack(None, 2)[0][2]

@pytest.fixture
def my_fixture():
    print("I am Fixture")

pytestmark = pytest.mark.usefixtures('my_fixture')


def test_my_fixture():
    print ("I'm the funtional test")


class Test:
    def test1(self):
        print ("I'm the class test - ", gfn())

    def test2(self):
        print ("I'm the class test - ", gfn())

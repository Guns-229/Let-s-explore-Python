# -*- coding: utf-8 -*-
"""
Created on Fri May 12 04:48:04 2017

@author: johri_m
"""
import pytest
import traceback


def gfn():
    return traceback.extract_stack(None, 2)[0][2]


@pytest.fixture
def my_fixture():
    print("MyFixture")


@pytest.mark.usefixtures('my_fixture')
def test_my_fixture():
    print("I'm the test")


@pytest.mark.usefixtures('my_fixture')
class Test:
    def test1(self):
        print("I'm the test 1")

    def test2(self):
        print("I'm the test 2")

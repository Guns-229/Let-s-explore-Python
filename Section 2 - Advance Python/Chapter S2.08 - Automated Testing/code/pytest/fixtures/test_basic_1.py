# -*- coding: utf-8 -*-

"""
Created on Fri May 12 04:44:10 2017
opts: -s -v 
@author: johri_m
"""
import pytest


@pytest.fixture
def basic_fixture():
    print("This is basic fixture")
    

def test_function(basic_fixture):
    print("This is dummy test function")


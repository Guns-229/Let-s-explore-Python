# -*- coding: utf-8 -*-

"""
Created on Fri May 12 04:44:10 2017
opts: -s -v 

this can be used to pass values to the function 

@author: johri_m
"""
import pytest

@pytest.fixture()
def my_fixture():
    data = {'x': 1, 'y': 2, 'z': 3}
    return data

def test_my_fixture(my_fixture):
    assert my_fixture['x'] == 1

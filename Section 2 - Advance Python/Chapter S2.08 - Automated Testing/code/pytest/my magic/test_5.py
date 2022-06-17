# -*- coding: utf-8 -*-
"""
Created on Sat May 13 08:06:17 2017

@author: johri_m
"""
import allure
import pytest

@pytest.mark.parametrize('issue, test', 
                         [('FOO-1', 1),
                          ('FOO-2', -3)])
def test_foo(issue, test):
    allure.mark_with_issue(issue)
    assert foo(test) > 0
# -*- coding: utf-8 -*-
"""
Created on Sat May 13 08:06:17 2017

@author: johri_m
"""

import pytest
import allure 
from allure.structure import TestCase, TestStep, Attach, TestSuite, Failure, TestLabel
#import pytest.allure 

@pytest.mark.parametrize('name, left, right', [['foo', 'a', 'a'],
                                               ['bar', 'a', 'b'],
                                               ['baz', 'b', 'b']])
def test_auto(name, left, right):
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_new(name, left, right):
        assert left == right, name
    
    TestStep("TEST")
    test_new(name, left, right)
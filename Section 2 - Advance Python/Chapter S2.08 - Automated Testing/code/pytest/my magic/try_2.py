# -*- coding: utf-8 -*-
"""
Created on Sat May 13 07:39:58 2017

@author: johri_m
"""

'''
This module shows some parametrization demos
'''
import pytest
import allure

@pytest.mark.parametrize('value', range(5))
def test_is_above_3(value):
    'checks that ``value`` is above 3'

    assert value > 3


@pytest.mark.parametrize('value', [
                                  1,
                                  2,
                                  5,
                                  pytest.mark.skipif(3),
                                  pytest.mark.xfail(0),
                                  pytest.mark.xfail(10)
                                  ])
def test_skip_xfail_in_parametrize(value):
    'same as above_3, but has some decorators'

    if(value == 5):
        allure.pytest_plugin.TestCase.__setattr__("Name", "EST")
    assert value > 3


@pytest.fixture(scope='function', params=['foo', 'bar', 'baz'])
def foo(request):
    return request.param


def test_fixture_parameters(foo):
    assert True

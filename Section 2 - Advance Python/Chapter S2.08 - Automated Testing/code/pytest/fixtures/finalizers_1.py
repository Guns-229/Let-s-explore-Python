# -*- coding: utf-8 -*-

"""
Created on Fri May 12 04:44:10 2017
opts: -s -v

If you want to run something after a test with a fixture has completed,
we can use finalizers. To do this, we get access to the request fixture
from pytest. A finalizer is a function inside a fixture that will run
after every test that a fixture is included.

@author: johri_m
"""
import pytest


@pytest.fixture()
def my_fixture(request):
    data = {'x': 1, 'y': 2, 'z': 3}

    def fin():
        print("Ending ...")
    request.addfinalizer(fin)

    return data


def test_my_fixture(my_fixture):
    assert my_fixture['x'] == 1

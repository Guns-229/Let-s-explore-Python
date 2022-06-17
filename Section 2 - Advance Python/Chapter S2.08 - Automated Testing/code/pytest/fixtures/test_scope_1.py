# -*- coding: utf-8 -*-

"""
Created on Fri May 12 04:44:10 2017
opts: -s -v 

scope of fixtures

    function: Run once per test
    class: Run once per class of tests
    module: Run once per module
    session: Run once per session


@author: johri_m
"""
import unittest
import pytest

@pytest.fixture(scope="class")
def db_class(request):
    class DummyDB:
        print("Dummy DB Creation")
        pass
    # set a class attribute on the invoking test context
    request.cls.db = DummyDB()
    


@pytest.mark.usefixtures("db_class")
class MyTest(unittest.TestCase):
    def test_method1(self):
        assert hasattr(self, "db")
        assert 0, self.db   # fail for demo purposes

    def test_method2(self):
        assert 0, self.db   # fail for demo purposes
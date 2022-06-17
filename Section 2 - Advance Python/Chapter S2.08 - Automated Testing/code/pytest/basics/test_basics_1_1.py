# -*- coding: utf-8 -*-
"""
Created on Fri May 12 04:25:52 2017.

Topic: Grouping Multiple Tests in a Class
execution command: -v
@author: johri_m
"""


class User:
    """."""
    name = "Nainjot"
    age = 32


class TestClass:
    """."""

    def test_string(self):
        x = "Mayank"
        assert 'a' in x

    def test_validate_attr_wrong(self):
        x = User
        assert hasattr(x, 'fullname')

    def test_validate_attr(self):
        x = User
        assert hasattr(x, 'name')

    def test_validate_attr_1(self):
        x = User
        assert hasattr(x, 'name')

    def testvalidate_attr(self):
        x = User
        assert hasattr(x, 'name')

    def t_validate_attr(self):
        x = User
        assert hasattr(x, 'name')

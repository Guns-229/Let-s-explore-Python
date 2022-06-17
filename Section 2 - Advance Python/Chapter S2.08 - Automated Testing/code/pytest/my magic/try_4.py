# -*- coding: utf-8 -*-
"""
Created on Sat May 13 08:06:17 2017

@author: johri_m
"""

import pytest
# import allure
import random
import string


def randomword(length):
    return ''.join(random.choice(string.ascii_lowercase)
                   for i in range(length))


@pytest.mark.parametrize('name, left, right', [['foo', 'a', 'a'],
                                               ['bar', 'a', 'b'],
                                               ['baz', 'b', 'b']])
def test_auto(name, left, right):

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_new(name, left, right):
        assert left == right, name
    # pytest.allure.severity_level

    def myd():
        print("Myd")
    # pytest.allure._allurelistener.test = myd()

    # allure_test.labels.append("<severity>pytest.allure.severity_level.CRITICAL</severity>")
    # print("Name: ", pytest.allure._allurelistener.test.name)
    # print(dir()
    # print(dir(allure.issue("TEST")))
    test_new(name, left, right)
    print(type(pytest.allure._allurelistener.test.labels))
    pytest.allure.story("TEST1")
# print("labels: ", pytest.allure._allurelistener.test.labels)
    # print("Name: ", pytest.allure._allurelistener.test.name)
    pytest.allure._allurelistener.test.name = "TEST_" + randomword(5)
    # allure_test = pytest.allure._allurelistener.test
    for lab, value in pytest.allure._allurelistener.test.labels:
        if "severity" in lab:
            print("lab")
            value = "critical"
        print(lab, value)


def teardown():
    print("HEEEEEELLLOOO")
    print(dir(pytest.allure._allurelistener.test))
    for lab, value in pytest.allure._allurelistener.test.labels:
        print(lab, value)
        if "severity" in lab:
            print("lab")
            value = "critical"
        print(lab, value)

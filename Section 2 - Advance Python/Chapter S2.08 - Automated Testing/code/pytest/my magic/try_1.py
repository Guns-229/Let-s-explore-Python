# -*- coding: utf-8 -*-
"""
Created on Fri May 12 04:44:10 2017
opts: -s -v
@author: johri_m
"""
import pytest
import allure

@pytest.fixture
def basic_fixture():
    print("This is basic fixture")


@pytest.fixture(autouse=True, scope="module")
def renamer(request):
    config = request.config
    my_super_suffix = 'ololo'
    print(dir(config.pluginmanager.get_plugins()))
    for a in config.pluginmanager.get_plugins():
        if(isinstance(a, allure.pytest_plugin.AllureAgregatingListener)):
            print(dir(a))
            print(a.suites)
    if hasattr(config, '_allurelistener'):
        print("changing Suite NAme")
        config._allurelistener.impl.testsuite.name += '[%s]' % my_super_suffix


def test_function(basic_fixture):
    print("This is dummy test function")

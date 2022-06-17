import allure
import pytest


class MyFancyStepTitle(object):
    def __init__(self, title):
        self.title = title

    def format(self, *a, **kw):
        return self.title.format(args=a, kwargs=kw)


@allure.step(MyFancyStepTitle("""Function called with args"""
                              """ {args}, kwargs {kwargs}"""))
def my_fancy_function(*a, **kw):
    return 'OK'


@pytest.hookimpl(trylast=True)
def pytest_configure(config):
    allure.environment(test_server='testserver', report='My Test Report')


@pytest.mark.parametrize("name, value",
                         [['foo', pytest.allure.severity_level.CRITICAL],
                          ['bar', pytest.allure.severity_level.BLOCKER],
                          ['baz', pytest.allure.severity_level.TRIVIAL]])
@allure.severity(pytest.allure.severity_level.CRITICAL)
def test_foo(name, value):
    # should produce step named
    my_fancy_function(1, 2, 3, foo='bar', baz='123')

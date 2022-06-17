import pytest


def pytest_addoption(parser):
    parser.addoption("--runsanity",
                     action="store_true",
                     help="run runsanity tests")
    parser.addoption("--nonahv", action="store_true", help="run non ahv tests")
    parser.addoption("--runupgrade",
                     action="store_true",
                     help="run all upgrade tests")
    parser.addoption("--rundefaultupgrade",
                     action="store_true",
                     help="run default upgrade tests")


def pytest_runtest_setup(item):
    if 'sanity' in item.keywords and not item.config.getvalue("runsanity"):
        print("Skipping test")
        pytest.skip("need --runslow option to run")

    else:
        print("\n" + "*" * 80)

        print("*" * 80)

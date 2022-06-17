import pytest


@pytest.fixture()
def my_fixture():
    print("This is a fixture")


def test_my_fixture(my_fixture):
    print("I'm the test")

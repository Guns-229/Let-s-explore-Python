import pytest

@pytest.fixture
def foo(request):
    def fin():
        print('Teardown of fixture foo')
    request.addfinalizer(fin)
    print("setup foo")
    return 42

@pytest.fixture
def bar(request):
    def fin():
        print('Teardown of fixture bar')
    request.addfinalizer(fin)
    print("inside bar ")

    return 7

def test_bar(foo, bar):
    assert foo != bar


def test_foo(foo):
    assert foo == 42


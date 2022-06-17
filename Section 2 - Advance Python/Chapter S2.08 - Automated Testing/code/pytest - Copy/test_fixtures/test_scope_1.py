import pytest 


@pytest.fixture(scope='session')
def foo(request):
    print('session setup')
    def fin():
        print('session finalizer')
    request.addfinalizer(fin)
    return f

@pytest.fixture(scope='function')  # default scope
def bar(request):
    print('funtion setup')
    def fin():
        print('function finalizer')
    request.addfinalizer(fin)
    return b

def test_one(foo, bar):
    pass

def test_two(foo, bar):
    pass
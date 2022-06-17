import pytest

@pytest.fixture
def foo():
    return 42

def test_foo(foo):
    assert foo == 42

class TestBar:
    @pytest.fixture
    def bar(self, request):
        def fin():
            print('Teardown of fixture bar')
        request.addfinalizer(fin)
        return 7

    def test_bar(self, foo, bar):
        assert foo != bar

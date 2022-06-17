import pytest


@pytest.mark.foo
@pytest.mark.parametrize(
    ("n", "expected"),
    [(1, 2), pytest.param(1, 3, marks=pytest.mark.sanity), (2, 3)])
def test_increment(n, expected):
    print(n, expected)
    assert n + 1 == expected

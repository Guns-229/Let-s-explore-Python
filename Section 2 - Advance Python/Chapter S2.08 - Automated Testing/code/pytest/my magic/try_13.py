import unittest

import pytest

class TestCase(object):

    @pytest.mark.parametrize("test_input,expected", [
    ("3+5", 8),
    ("2+4", 6),
    ("6*9", 42),
    ])
    def test_1(self, a, b):
        assert eval(a) == b
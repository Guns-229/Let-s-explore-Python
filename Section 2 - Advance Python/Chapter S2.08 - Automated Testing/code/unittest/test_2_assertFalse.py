import unittest


class Mylibrary():
    __version__ = 1

    def multiply(a, b):
        """
        >>> multiply(4, 3)
        12
        >>> multiply('a', 3)
        'aaa'
        """
        return a * b

    def subtraction(a, b):
        """
        >>> subtraction(4, 3)
        1
        >>> multiply(-1, 3)
        -4
        """
        return a - b


class SubTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_numbers_3_4(self):
        self.assertEqual(Mylibrary.subtraction(3, 4), -1)


class TestUM(unittest.TestCase):

    def setUp(self):
        pass

    def test_numbers_3_4(self):
        self.assertEqual(Mylibrary.multiply(3, 4), 12)

    def test_strings_a_3(self):
        self.assertEqual(Mylibrary.multiply('a', 3), 'aaa')

    def test_others_1(self):
        a = d = 10
        b = 12
        c = 10
        self.assertEqual(a, a)
        self.assertEqual(a, b)
        self.assertEqual(a, c)
        self.assertEqual(a, d)

    def test_others_a_a(self):
        a = 10
        self.assertEqual(a, a)

    def test_others_a_b(self):
        a = 10
        b = 12
        self.assertEqual(a, b)

    def test_others_a_c(self):
        a = 10
        c = 10
        self.assertEqual(a, c)

    def test_others_a_d(self):
        a = d = 10
        self.assertEqual(a, d)


if __name__ == '__main__':
    unittest.main()

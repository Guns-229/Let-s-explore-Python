import unittest

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
    
 
class TestUM(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_numbers_3_4(self):
        self.assertEqual(multiply(3,4), 12)
 
    def test_strings_a_3(self):
        self.assertEqual( multiply('a',3), 'aaa', "good work")
        
    def test_strings_a_b(self):
        self.assertFail(multiply('a','b'))

class TestUMSubtraction(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_numbers_3_4(self):
        self.assertEqual(subtraction(3,4), -1)
 
    
 
if __name__ == '__main__':
    unittest.main()
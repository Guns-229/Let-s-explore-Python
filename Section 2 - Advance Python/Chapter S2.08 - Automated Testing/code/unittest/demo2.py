# Run Examples from command line 
import unittest

def multiply(a, b):
    """
    >>> multiply(4, 3)
    12
    >>> multiply('a', 3)
    'aaa'
    """
    return a * b
    
 
class TestUM(unittest.TestCase):
 
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_numbers_3_4(self):
        self.assertEqual(multiply(3, 4), 12)
 
    def test_strings_a_3(self):
        self.assertEqual(multiply('a', 3), 'aaa')
        
    def test_strings_3_A(self):
        self.assertEqual(multiply(3, 'A'), 'aaa')

    def test_strings_3_A_fixed(self):
        self.assertEqual(multiply(3, 'A'), 'AAA')
                
    def test_string_a_b(self):
        self.assertFalse(multiply('a', 'b'), 'ab')


if __name__ == '__main__':
    unittest.main()

import unittest
import sys


class Mylibrary:
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
    
 
class TestUM(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_numbers_3_4(self):
        self.assertEqual( Mylibrary.multiply(3,4), 12)
 
    def test_strings_a_3(self):
        self.assertEqual(Mylibrary.multiply('a',3), 'aaa')
    
    @unittest.skip("demonstrating skipping")
    def test_string_a_b(self):
        self.assertRaises(TypeError, multiply('a','b'))
        
    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_windows_support(self):
        # windows specific testing code
        pass

    @unittest.skipIf(Mylibrary.__version__ < 1.2, 
                     "not supported in this library version")
    def test_format(self):
        # Tests that work for only a certain version of the library.
        pass


    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(1, 0, "broken")
    
 
if __name__ == '__main__':
    unittest.main()
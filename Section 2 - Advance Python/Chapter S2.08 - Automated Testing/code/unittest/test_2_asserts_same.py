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
    
    def returnval(a):
        
        return("Hello") 
 
class TestUM(unittest.TestCase):
    
    
    def setUp(self):
        pass
 
    def test_numbers_3_4(self):
        self.assertIs(Mylibrary.multiply(3,4), 12)
    
    def test_others_a_a(self):
        a = 10
        self.assertIs(a, a)
        
    def test_others_a_b(self):
        a = 10
        b = 12
        print(self.assertIs(a, b))
        
    def test_others_a_c(self):
        a = 10
        c = 2*5
        print(id(a), id(c))
        self.assertIs(a, c)
        
    def test_others_a_myval(self):
        a = "Hello"
        
        self.assertIs(a, Mylibrary.returnval(2))
        
    def test_others_a_d(self):
        a = d = 10
        print(self.assertIs(a,d))
    

        
 
    
 
if __name__ == '__main__':
    unittest.main()
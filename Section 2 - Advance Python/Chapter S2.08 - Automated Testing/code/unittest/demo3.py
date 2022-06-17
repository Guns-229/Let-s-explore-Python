import unittest

def test_mytest():
    """this will never run"""
    print("test_mytest")

class D():
	pass

def reut():
	return 10
	
	
class TestStringMethods(unittest.TestCase):

 	def test_equal(self):
		a = [reut()]
		b = [10]
		print(id(a), id(b))
		self.assertEqual(a, b)
		
 	def test_is_fail(self):
		a = [reut()]
		b = [10]
		print(id(a), id(b))
		self.assertIs(a, b)
	
	
	def test_isNot(self):
		a = [reut()]
		b = [10]
		print(id(a), id(b))
		self.assertIsNot(a, b)
	
	
	def test_is(self):
		c = d = D()
		print(id(c), id(d))
		self.assertIs(c,d)
		
if __name__ == '__main__':
    unittest.main()


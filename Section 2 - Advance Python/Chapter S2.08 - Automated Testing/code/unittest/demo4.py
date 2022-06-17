import unittest

class A():
	pass

class D():
	pass


def reut():
	return 10
	
	
class TestDemo(unittest.TestCase):

 	def test_instance(self):
		a = D()
		self.assertIsInstance(a, D)
	
	def test_assertNotIsInstance(self):
		a = A()
		self.assertNotIsInstance(a, D)
	
	def test_assertNotIsInstance_Fail(self):
		a = A()
		self.assertNotIsInstance(a, A)

	
if __name__ == '__main__':
    unittest.main()


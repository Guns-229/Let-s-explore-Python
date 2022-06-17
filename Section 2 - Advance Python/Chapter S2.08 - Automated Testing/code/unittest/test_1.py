import unittest

def test_mytest():
    """this will never run"""
    print("test_mytest")

class D():
	pass

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        print(s)
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

	def test_is_and(self):
		a = D()
		b = D()
		print(self.assertEqual(a,b))
		c = d = D()
		print(self.assertIs(c,d))

    def test_mymymy(self):
        print("TESTTEST")

		
		
if __name__ == '__main__':
    unittest.main()


import unittest
import sys


class MyTestCase(unittest.TestCase):
    def setUp(self):
        print("Running:", self.id())  # .split('.')[-1])

    def test_nothing(self):
        self.fail("Successfully testing nothing")

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_windows_support(self):
        # windows specific testing code
        pass


if __name__ == '__main__':
    unittest.main()
# self.skipTest("another method for skipping")

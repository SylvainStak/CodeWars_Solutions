import unittest
from problem import *

class Test(unittest.TestCase):
    def tests(self):
        tests = (
            ("John", "Hello, John!"),
            ("aLIce", "Hello, Alice!"),
            ("", "Hello, World!"),
        )

        for inp, exp in tests:
            self.assertEqual(hello(inp), exp)
        self.assertEqual(hello(), "Hello, World!")

if __name__ == '__main__':
   unittest.main()

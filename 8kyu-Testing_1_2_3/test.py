import unittest
from problem import *

class Test(unittest.TestCase):
    def tests(self):
        self.assertEqual(number([]), [])
        self.assertEqual(number(["a", "b", "c"]), ["1: a", "2: b", "3: c"])

if __name__ == '__main__':
   unittest.main();

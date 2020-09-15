import unittest
from problem import *

class Test(unittest.TestCase):
    def tests(self):
        self.assertEqual(add(2,11), 13)
        self.assertEqual(add(0,1), 1)
        self.assertEqual(add(0,0), 0)
        self.assertEqual(add(16,18), 214)
        self.assertEqual(add(26,39), 515)
        self.assertEqual(add(122,81), 1103)

if __name__ == '__main__':
   unittest.main()

import unittest
from problem import *

class Test(unittest.TestCase):
    def tests(self):
        self.assertEqual(stem_and_leaf([11, 35, 14, 9, 39, 23, 35]), {0: [9], 1: [1, 4], 2: [3], 3: [5, 5, 9]})

if __name__ == '__main__':
   unittest.main()
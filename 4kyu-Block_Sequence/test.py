import unittest
from problem import *

class Test(unittest.TestCase):
    def tests(self):
        self.assertEqual(solve(1), 1)
        self.assertEqual(solve(2), 1)
        self.assertEqual(solve(3), 2)
        self.assertEqual(solve(100), 1)
        self.assertEqual(solve(2100), 2)
        self.assertEqual(solve(31000), 2) 
        self.assertEqual(solve(999999999999999999), 4) 
        self.assertEqual(solve(1000000000000000000), 1)
        self.assertEqual(solve(999999999999999993), 7)

if __name__ == '__main__':
   unittest.main()

import unittest
from problem import *

class Test(unittest.TestCase):
    def tests(self):
        self.assertEqual(pairs([1,2,5,8,-4,-3,7,6,5]),3)
        self.assertEqual(pairs([21, 20, 22, 40, 39, -56, 30, -55, 95, 94]),2)
        self.assertEqual(pairs([81, 44, 80, 26, 12, 27, -34, 37, -35]),0)
        self.assertEqual(pairs([-55, -56, -7, -6, 56, 55, 63, 62]),4)
        self.assertEqual(pairs([73, 72, 8, 9, 73, 72]),3)

if __name__ == '__main__':
   unittest.main()

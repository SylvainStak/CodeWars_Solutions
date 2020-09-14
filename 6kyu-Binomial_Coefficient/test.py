import unittest
from problem import *

class Test(unittest.TestCase):
    def tests(self):
        self.assertEqual(choose(1,1),1)
        self.assertEqual(choose(5,4),5)
        self.assertEqual(choose(10,5),252)
        self.assertEqual(choose(10,20),0)
        self.assertEqual(choose(52,5),2598960)

if __name__ == '__main__':
   unittest.main()

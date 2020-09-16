import unittest
from problem import *

class Test(unittest.TestCase):
    def tests(self):
        self.assertEqual(sakura_fall(5), 80)
        self.assertEqual(sakura_fall(10), 40)
        self.assertEqual(sakura_fall(-1), 0)
if __name__ == '__main__':
   unittest.main()

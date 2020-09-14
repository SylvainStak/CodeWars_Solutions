import unittest
from problem import *

class Test(unittest.TestCase):
    def tests(self):
        self.assertEqual(digital_root(16), 7)
        self.assertEqual(digital_root(942), 6)
        self.assertEqual(digital_root(132189), 6)
        self.assertEqual(digital_root(493193), 2)

if __name__ == '__main__':
   unittest.main();

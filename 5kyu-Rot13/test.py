import unittest
from problem import *

class Test(unittest.TestCase):
    def tests(self):
        self.assertEqual(rot13("test"),"grfg")
        self.assertEqual(rot13("Test"),"Grfg")

if __name__ == '__main__':
   unittest.main();

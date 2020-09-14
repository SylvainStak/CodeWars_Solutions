import unittest
from problem import *

class Test(unittest.TestCase):
    def tests(self):
        self.assertEqual(ips_between("10.0.0.0", "10.0.0.50"), 50)
        self.assertEqual(ips_between("10.0.0.0", "10.0.1.0"), 256)     
        self.assertEqual(ips_between("20.0.0.10", "20.0.1.0"), 246)

if __name__ == '__main__':
   unittest.main()

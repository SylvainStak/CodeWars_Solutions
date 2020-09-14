import unittest
from problem import *

class Test(unittest.TestCase):
    def tests(self):
        self.assertEquals(narcissistic(7), True, '7 is narcissistic');
        self.assertEquals(narcissistic(371), True, '371 is narcissistic');
        self.assertEquals(narcissistic(122), False, '122 is not narcissistic')
        self.assertEquals(narcissistic(4887), False, '4887 is not narcissistic')

if __name__ == '__main__':
   unittest.main()

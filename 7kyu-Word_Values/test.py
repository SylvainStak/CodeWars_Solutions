import unittest
from problem import *

class Test(unittest.TestCase):
    def tests(self):
        self.assertEqual(name_value(["abc","abc","abc","abc"]),[6,12,18,24])
        self.assertEqual(name_value(["codewars","abc","xyz"]),[88,12,225])


if __name__ == '__main__':
   unittest.main()

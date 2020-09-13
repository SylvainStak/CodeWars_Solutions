import unittest
from problem import *

class Test(unittest.TestCase):
	def tests(self):
		self.assertEqual(is_divisible(3,3,4),False)
		self.assertEqual(is_divisible(12,3,4),True)
		self.assertEqual(is_divisible(8,3,4),False)
		self.assertEqual(is_divisible(48,3,4),True)

if __name__ == '__main__':
   unittest.main();

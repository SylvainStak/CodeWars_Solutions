import unittest
from problem import *

class Test(unittest.TestCase):
    def tests(self):
        self.assertEqual(get_turkish_number(1), "bir")
        self.assertEqual(get_turkish_number(13), "on üç")
        self.assertEqual(get_turkish_number(27), "yirmi yedi")
        self.assertEqual(get_turkish_number(38), "otuz sekiz")
        self.assertEqual(get_turkish_number(77), "yetmiş yedi")
        self.assertEqual(get_turkish_number(94), "doksan dört")
if __name__ == '__main__':
   unittest.main()

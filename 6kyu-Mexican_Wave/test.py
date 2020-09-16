import unittest
from problem import *

class Test(unittest.TestCase):
    def tests(self):
        result = ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
        self.assertEqual(wave("hello"), result)
        result = ["Codewars", "cOdewars", "coDewars", "codEwars", "codeWars", "codewArs", "codewaRs", "codewarS"]
        self.assertEqual(wave("codewars"), result)
        result = []
        self.assertEqual(wave(""), result)
        result = [" Gap ", " gAp ", " gaP "]
        self.assertEqual(wave(" gap "), result)
        result = ["Two words", "tWo words", "twO words", "two Words", "two wOrds", "two woRds", "two worDs", "two wordS"]
        self.assertEqual(wave("two words"),result)
        

if __name__ == '__main__':
   unittest.main()
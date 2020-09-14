import unittest
from problem import *

class Test(unittest.TestCase):
    def tests(self):
        self.assertEqual(dative('ablak'), 'ablaknak')
        self.assertEqual(dative('tükör'), 'tükörnek')
        self.assertEqual(dative('keret'), 'keretnek')
        self.assertEqual(dative('otthon'), 'otthonnak')
        self.assertEqual(dative('virág'), 'virágnak')
        self.assertEqual(dative('tett'), 'tettnek')
        self.assertEqual(dative('rokkant'), 'rokkantnak')
        self.assertEqual(dative('rossz'), 'rossznak')

if __name__ == '__main__':
   unittest.main();

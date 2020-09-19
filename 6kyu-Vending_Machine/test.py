import unittest
from problem import *

class Test(unittest.TestCase):
    def tests(self):
        items = [{'name':"Smarties", 'code':"A01", 'quantity':10, 'price':0.60},
         {'name':"Caramac Bar", 'code':"A02", 'quantity':5, 'price':0.60},
         {'name':"Dairy Milk", 'code':"A03", 'quantity':1, 'price':0.65},
         {'name':"Freddo", 'code':"A04", 'quantity':1, 'price':0.25}]

        machine = VendingMachine(items, 10.0)
        self.assertEqual(machine.vend("A01",0.60), "Vending Smarties")
        self.assertEqual(machine.vend("A01",10.0), "Vending Smarties with 9.40 change.")
        self.assertEqual(machine.vend("Z01",0.41), "Invalid selection! : Money in vending machine = 11.20")
        self.assertEqual(machine.vend("A02",0.40), "Not enough money!")


if __name__ == '__main__':
   unittest.main()

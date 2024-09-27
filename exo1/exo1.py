"""
We want to have a new class Item such as :

A new item can be created with Item(price, weight)
    The price and weight of an item can be accessed with
    item.price and item.weight.
    Write the code for this class, with the appropriate constructor.
Example of code using the class: i = Item(10, 20)
"""
import unittest


class Item:

    def __init__(self, price, weight):
        self.price=price
        self.weight =weight

class Exo1Test(unittest.TestCase):

    def test_item_construction(self):
        item = Item(10, 20)

        self.assertEqual(20, item.weight)
        self.assertEqual(10, item.price)

# Si vous exécutez ce fichier directement, cela exécutera les tests
if __name__ == '__main__':
    unittest.main()
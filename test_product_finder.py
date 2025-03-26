# test_product_finder.py
import unittest
import datetime
from ProductFinder import get_price_changes

class TestPriceChange(unittest.TestCase):

    def test_price_change_within_last_month(self):
        price_changes = get_price_changes('Products.txt', "Product1")
        self.assertEqual(len(price_changes), 2)
        self.assertEqual(price_changes[0][1], 200.0)
        self.assertEqual(price_changes[1][1], 160.0)

    def test_no_price_change_for_nonexistent_product(self):
        price_changes = get_price_changes('Products.txt', "Product4")
        self.assertEqual(len(price_changes), 0)

    def test_file_not_found(self):
        price_changes = get_price_changes('nonexistent_file.txt', "Товар 1")
        self.assertEqual(len(price_changes), 0)

if __name__ == '__main__':
    unittest.main()

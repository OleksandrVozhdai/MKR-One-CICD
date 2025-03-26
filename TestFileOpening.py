import unittest
from unittest.mock import patch, mock_open
from ProductFinder import get_price_changes

class TestFileOpening(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data="Product1, 2025-03-20, 200.0\nProduct1, 2025-03-01, 160.0\n")
    def test_file_opening_and_reading(self, mock_file):

        product_changes = get_price_changes('products.txt', 'Product1')

        mock_file.assert_called_with('products.txt', 'r')

        self.assertEqual(len(product_changes), 2)
        self.assertEqual(product_changes[0][1], 200.0)
        self.assertEqual(product_changes[1][1], 160.0)

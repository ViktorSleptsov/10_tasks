import unittest
from converter import convert


class TestConverter(unittest.TestCase):
    def test_usd(self):
        self.assertAlmostEqual(convert(9200, "USD"), 100.0)

    def test_eur(self):
        self.assertAlmostEqual(convert(10000, "EUR"), 100.0)

    def test_cny(self):
        self.assertAlmostEqual(convert(1270, "CNY"), 100.0)

    def test_bad_currency(self):
        with self.assertRaises(ValueError):
            convert(1000, "GBP")

    def test_negative(self):
        with self.assertRaises(ValueError):
            convert(-1, "USD")


if __name__ == "__main__":
    unittest.main()
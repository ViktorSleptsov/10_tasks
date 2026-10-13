import unittest
from number_to_words import number_to_words


class TestNumberToWords(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(number_to_words(5), "Пять")

    def test_teen(self):
        self.assertEqual(number_to_words(15), "Пятнадцать")

    def test_hundreds(self):
        self.assertEqual(number_to_words(247), "Двести сорок семь")

    def test_thousand(self):
        self.assertEqual(number_to_words(1000), "Тысяча")

    def test_out_of_range(self):
        with self.assertRaises(ValueError):
            number_to_words(0)

    def test_out_of_range_high(self):
        with self.assertRaises(ValueError):
            number_to_words(1001)


if __name__ == "__main__":
    unittest.main()
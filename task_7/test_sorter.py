import unittest
from sorter import parse_numbers, sort_asc, sort_desc, stats


class TestSorter(unittest.TestCase):
    def test_parse(self):
        self.assertEqual(parse_numbers("5 2 9"), [5.0, 2.0, 9.0])

    def test_parse_bad(self):
        with self.assertRaises(ValueError):
            parse_numbers("5 abc 9")

    def test_parse_empty(self):
        with self.assertRaises(ValueError):
            parse_numbers("   ")

    def test_sort_asc(self):
        self.assertEqual(sort_asc([5, 2, 9, 1]), [1, 2, 5, 9])

    def test_sort_desc(self):
        self.assertEqual(sort_desc([5, 2, 9, 1]), [9, 5, 2, 1])

    def test_stats(self):
        s = stats([1, 2, 3, 4])
        self.assertEqual(s["min"], 1)
        self.assertEqual(s["max"], 4)
        self.assertEqual(s["sum"], 10)
        self.assertEqual(s["avg"], 2.5)


if __name__ == "__main__":
    unittest.main()
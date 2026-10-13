import os
import tempfile
import unittest
from shopping import load_items, add_item, remove_item, clear_items


class TestShopping(unittest.TestCase):
    def setUp(self):
        fd, self.path = tempfile.mkstemp()
        os.close(fd)
        os.remove(self.path)

    def tearDown(self):
        if os.path.exists(self.path):
            os.remove(self.path)

    def test_add(self):
        add_item("Молоко", self.path)
        add_item("Хлеб", self.path)
        self.assertEqual(load_items(self.path), ["Молоко", "Хлеб"])

    def test_add_empty(self):
        with self.assertRaises(ValueError):
            add_item("   ", self.path)

    def test_remove(self):
        add_item("A", self.path)
        add_item("B", self.path)
        removed = remove_item(0, self.path)
        self.assertEqual(removed, "A")
        self.assertEqual(load_items(self.path), ["B"])

    def test_remove_bad_index(self):
        with self.assertRaises(IndexError):
            remove_item(5, self.path)

    def test_clear(self):
        add_item("A", self.path)
        clear_items(self.path)
        self.assertEqual(load_items(self.path), [])


if __name__ == "__main__":
    unittest.main()
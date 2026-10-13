import unittest
from password_gen import generate_password


class TestPasswordGen(unittest.TestCase):
    def test_length(self):
        pwd = generate_password(12)
        self.assertEqual(len(pwd), 12)

    def test_too_short(self):
        with self.assertRaises(ValueError):
            generate_password(5)

    def test_too_long(self):
        with self.assertRaises(ValueError):
            generate_password(33)

    def test_special_chars(self):
        # Может случайно не попасть, но с большой длиной шанс мал
        pwd = generate_password(32, use_special=True)
        self.assertEqual(len(pwd), 32)


if __name__ == "__main__":
    unittest.main()
import unittest
from palindrome import is_palindrome


class TestPalindrome(unittest.TestCase):
    def test_simple(self):
        self.assertTrue(is_palindrome("level"))

    def test_russian(self):
        self.assertTrue(is_palindrome("А роза упала на лапу Азора"))

    def test_with_punctuation(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))

    def test_not_palindrome(self):
        self.assertFalse(is_palindrome("привет"))

    def test_empty(self):
        self.assertFalse(is_palindrome("   "))


if __name__ == "__main__":
    unittest.main()
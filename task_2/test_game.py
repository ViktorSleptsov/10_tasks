import unittest
from guess_game import check_guess, make_secret


class TestGuess(unittest.TestCase):
    def test_more(self):
        self.assertEqual(check_guess(50, 25), "more")

    def test_less(self):
        self.assertEqual(check_guess(50, 75), "less")

    def test_win(self):
        self.assertEqual(check_guess(50, 50), "win")

    def test_range(self):
        for _ in range(100):
            n = make_secret()
            self.assertTrue(1 <= n <= 100)


if __name__ == "__main__":
    unittest.main()
import unittest
from datetime import date
from season import parse_date, get_season, get_weekday, days_to_end_of_year


class TestSeason(unittest.TestCase):
    def test_parse(self):
        self.assertEqual(parse_date("15.07.2025"), date(2025, 7, 15))

    def test_parse_bad(self):
        with self.assertRaises(ValueError):
            parse_date("2025-07-15")

    def test_season_summer(self):
        self.assertEqual(get_season(date(2025, 7, 15)), "Лето")

    def test_season_winter(self):
        self.assertEqual(get_season(date(2025, 1, 10)), "Зима")

    def test_weekday(self):
        self.assertEqual(get_weekday(date(2025, 7, 15)), "Вторник")

    def test_days_left(self):
        # 31 декабря — 0 дней до конца года
        self.assertEqual(days_to_end_of_year(date(2025, 12, 31)), 0)
        # 1 января — 364 дня (не високосный)
        self.assertEqual(days_to_end_of_year(date(2025, 1, 1)), 364)


if __name__ == "__main__":
    unittest.main()
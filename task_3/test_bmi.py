import unittest
from bmi import calculate_bmi, bmi_category


class TestBMI(unittest.TestCase):
    def test_normal(self):
        self.assertAlmostEqual(calculate_bmi(70, 1.75), 22.86, places=2)

    def test_category_low(self):
        self.assertEqual(bmi_category(17), "Недостаток")

    def test_category_normal(self):
        self.assertEqual(bmi_category(22), "Норма")

    def test_category_over(self):
        self.assertEqual(bmi_category(27), "Избыток")

    def test_category_obese(self):
        self.assertEqual(bmi_category(35), "Ожирение")

    def test_zero_height(self):
        with self.assertRaises(ValueError):
            calculate_bmi(70, 0)


if __name__ == "__main__":
    unittest.main()
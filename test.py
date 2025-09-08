import unittest
from main import remainder

class TestRemainder(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(remainder(10, 3), 1)

    def test_dividend_less_than_divisor(self):
        self.assertEqual(remainder(2, 5), 2)

    def test_divisible_numbers(self):
        self.assertEqual(remainder(9, 3), 0)

    def test_negative_numbers(self):
        self.assertEqual(remainder(-10, 3), -10 % 3)
        self.assertEqual(remainder(10, -3), 10 % -3)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            remainder(5, 0)

if __name__ == "__main__":
    unittest.main()


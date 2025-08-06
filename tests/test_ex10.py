import unittest
from datetime import datetime, timedelta

from exercicios.ex10 import GigasecondCalculator


class TestGigasecondCalculator(unittest.TestCase):
    def test_default_date(self):
        start_date = datetime(2025, 8, 6, 10, 14)
        expected = start_date + timedelta(seconds=1_000_000_000)
        calculator = GigasecondCalculator(start_date)
        result = calculator.calculate()
        self.assertEqual(result, expected)

    def test_new_year_edge_case(self):
        start_date = datetime(1999, 12, 31, 23, 59)
        expected = start_date + timedelta(seconds=1_000_000_000)
        calculator = GigasecondCalculator(start_date)
        result = calculator.calculate()
        self.assertEqual(result, expected)

    def test_different_dates_should_give_different_results(self):
        date1 = datetime(2000, 1, 1)
        date2 = datetime(2010, 1, 1)
        result1 = GigasecondCalculator(date1).calculate()
        result2 = GigasecondCalculator(date2).calculate()
        self.assertNotEqual(result1, result2)


if __name__ == "__main__":
    unittest.main()
    unittest.main()

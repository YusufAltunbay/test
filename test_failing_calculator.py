import unittest

from failing_calculator import average_ratios


class TestAverageRatios(unittest.TestCase):
    def test_ignores_zero_values(self):
        self.assertEqual(average_ratios([10, 5, 0]), 15.0)

    def test_raises_when_all_values_are_zero(self):
        with self.assertRaises(ValueError):
            average_ratios([0, 0, 0])

    def test_raises_for_empty_list(self):
        with self.assertRaises(ValueError):
            average_ratios([])

    def test_raises_for_non_numeric_items(self):
        with self.assertRaises(TypeError):
            average_ratios([10, "x"])


if __name__ == "__main__":
    unittest.main()

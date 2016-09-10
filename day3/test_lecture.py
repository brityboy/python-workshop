import unittest
from lecture import foo, median_after_throwing_out_outliers

class ScratchTests(unittest.TestCase):
    def test_foo(self):
        expected = 7
        result = foo(6)
        self.assertEqual(expected, result)

    def test_foo_negative_numbers(self):
        expected = -7
        result = foo(-8)
        self.assertEqual(expected, result)

    def test_median(self):
        l = [1, 3, 5]
        expected = 3
        result = median_after_throwing_out_outliers(l)
        self.assertEqual(expected, result)

    def test_median_even(self):
        l = [1, 3, 5, 7]
        expected = 4
        result = median_after_throwing_out_outliers(l)
        self.assertEqual(expected, result)

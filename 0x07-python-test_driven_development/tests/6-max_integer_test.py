#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    This class contains methods testing a max_integer function
    """
    def test_empty_list(self):
        """
        testing empty list
        """
        result = max_integer([])
        self.assertIsNone(result)

    def test_positive_numbers(self):
        """
        Testing list, all +ve
        """
        result = max_integer([1, 2, 3, 4, 5])
        self.assertEqual(result, 5)

    def test_negative_numbers(self):
        """
        all -ve
        """
        result = max_integer([-1, -2, -3, -4, -5])
        self.assertEqual(result, -1)

    def test_mixed_numbers(self):
        """
        +ve and -ve
        """
        result = max_integer([-5, 0, 10, -2, 8])
        self.assertEqual(result, 10)

    def test_duplicate_numbers(self):
        """
        Duplicate numbers
        """
        result = max_integer([5, 5, 5, 5, 5])
        self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()

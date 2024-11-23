# A unsorted array of integers is given;
# you need to find the max product formed my multiplying three numbers.
# (You cannot sort the array, watch out when there are negative numbers)

import unittest


def highest_product_of_3(arr):
    if len(arr) < 3 or arr is None:
        raise Exception("Invalid input")

    highest = max(arr[0], arr[1])
    lowest = min(arr[0], arr[1])
    max_product_of_two = arr[0] * arr[1]
    min_product_of_two = arr[0] * arr[1]
    product_of_three = arr[0] * arr[1] * arr[2]

    for i in range(2, len(arr)):
        product_of_three = max(product_of_three, max_product_of_two * arr[i], min_product_of_two * arr[i])
        max_product_of_two = max(max_product_of_two, highest * arr[i], lowest * arr[i])
        min_product_of_two = min(min_product_of_two, highest * arr[i], lowest * arr[i])
        highest = max(highest, arr[i])
        lowest = min(lowest, arr[i])

    return product_of_three


class Test(unittest.TestCase):

    def test_short_list(self):
        actual = highest_product_of_3([1, 2, 3, 4])
        expected = 24
        self.assertEqual(actual, expected)

    def test_longer_list(self):
        actual = highest_product_of_3([6, 1, 3, 5, 7, 8, 2])
        expected = 336
        self.assertEqual(actual, expected)

    def test_list_has_one_negative(self):
        actual = highest_product_of_3([-5, 4, 8, 2, 3])
        expected = 96
        self.assertEqual(actual, expected)

    def test_list_has_two_negatives(self):
        actual = highest_product_of_3([-10, 1, 3, 2, -10])
        expected = 300
        self.assertEqual(actual, expected)

    def test_list_is_all_negatives(self):
        actual = highest_product_of_3([-5, -1, -3, -2])
        expected = -6
        self.assertEqual(actual, expected)

    def test_error_with_empty_list(self):
        with self.assertRaises(Exception):
            highest_product_of_3([])

    def test_error_with_one_number(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1])

    def test_error_with_two_numbers(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1, 1])


unittest.main(verbosity=2)

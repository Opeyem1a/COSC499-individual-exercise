import unittest

from sort_integers.sort_integers import sort_integers


class TestSortIntegers(unittest.TestCase):
    def test_sort_integers(self):
        input_integers_list = [3, 4, 1, 2]
        sorted_list = sort_integers(input_integers_list)
        sorted_list_expected = [1, 2, 3, 4]
        self.assertListEqual(sorted_list, sorted_list_expected)

    def test_sort_integers_doesnt_modify_original_list(self):
        input_integers_list = [3, 4, 1, 2]
        sorted_list = sort_integers(input_integers_list)
        self.assertNotEqual(sorted_list, input_integers_list)

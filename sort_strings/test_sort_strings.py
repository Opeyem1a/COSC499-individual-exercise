import unittest

from sort_strings.sort_strings import sort_strings


class TestSortStrings(unittest.TestCase):
    def test_sort_strings(self):
        input_strings_list = ['B', 'BC', 'A', 'AB']
        sorted_list = sort_strings(input_strings_list)
        sorted_list_expected = ['A', 'AB', 'B', 'BC']
        self.assertListEqual(sorted_list, sorted_list_expected)

    def test_sort_integers_doesnt_modify_original_list(self):
        input_strings_list = ['B', 'BC', 'A', 'AB']
        sorted_list = sort_strings(input_strings_list)
        self.assertNotEqual(sorted_list, input_strings_list)

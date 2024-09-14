from unittest import TestCase


class MyTestCase(TestCase):


    def test_for_biggest_Numbers_in_a_list(self):
        numbers_list = ([2,3,6,7,8])
        expected_number = 8
        self.assertEqual(smallestandlargestnumbers.biggest_number(numbers_list), expected_number)

    def test_for_smallest_Numbers_in_a_list(self):
        numbers_list = ([2,3,6,7,8])
        expected_number = 2
        self.assertEqual(smallestandlargestnumbers.smallest_number(numbers_list), expected_number)


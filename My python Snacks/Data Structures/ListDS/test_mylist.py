import unittest

from DataStructures.ListDS.my_list import MyList


class TestList(unittest.TestCase):


    def setUp(self):
        self.my_list = MyList()



    def test_elements_can_be_appended_to_list(self):
        self.my_list.append_element(10)
        self.my_list.append_element(20)
        self.assertEqual(self.my_list.get_index(0), 10)
        self.assertEqual(self.my_list.get_index(1), 20)


    def test_insert_valid(self):
        self.my_list.append_element(1)
        self.my_list.append_element(3)
        self.my_list.insert(1, 2)
        self.assertEqual(self.my_list.get_index(1), 2)


    def test_insert_out_of_bounds(self):
        with self.assertRaises(IndexError):
            self.my_list.insert(2, 4)  # Out of bounds


    def test_remove_existing_element(self):
        self.my_list.append_element(1)
        self.my_list.append_element(2)
        self.my_list.remove(1)
        self.assertEqual(self.my_list.get_index(0), 2)


    def test_remove_non_existing_element(self):
        with self.assertRaises(ValueError):
            self.my_list.remove(30)


    def test_pop_last_element(self):
        self.my_list.append_element(1)
        self.assertEqual(self.my_list.pop(), 1)  # Pop last item


    def test_pop_specific_index(self):
        self.my_list.append_element(1)
        self.my_list.append_element(2)
        self.assertEqual(self.my_list.pop(0), 1)  # Pop index 0


    def test_pop_from_empty_list(self):
        with self.assertRaises(IndexError):
            self.my_list.pop()


    def test_get_valid_index(self):
        self.my_list.append_element(1)
        self.assertEqual(self.my_list.get_index(0), 1)


    def test_get_invalid_index(self):
        with self.assertRaises(IndexError):
            self.my_list.get_index(1)  # Index out of bounds


    def test_size(self):
        self.my_list.append_element(20)
        self.assertEqual(self.my_list.get_list_size(), 1)


    def test_is_empty(self):
        self.assertTrue(self.my_list.is_empty())
        self.my_list.append_element(1)
        self.assertFalse(self.my_list.is_empty())





if __name__ == '__main__':
    unittest.main()

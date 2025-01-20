import unittest

import stack



class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = stack.Stack()



    def test_stack_can_push_elements_and_peek_to_verify_top_element(self):
        self.stack.append_element(1)
        self.stack.append_element(2)
        self.stack.peek_element()
        self.assertEqual(self.stack.peek_element(), 2)


    def test_stack_can_push_and_pop_all_elements(self):
        self.stack.append_element(1)
        self.stack.append_element(2)
        self.stack.append_element(3)
        self.stack.append_element(4)
        self.assertEqual(self.stack.pop_element(), 4)
        self.assertEqual(self.stack.pop_element(), 3)
        self.assertEqual(self.stack.pop_element(), 2)
        self.assertEqual(self.stack.pop_element(), 1)
        self.assertEqual(self.stack.is_empty(), True)



    def test_that_stack_can_push_3elements_pop2_and_peek_to_find_1_element(self):
        self.stack.append_element(1)
        self.stack.append_element(2)
        self.stack.append_element(3)
        self.assertEqual(self.stack.pop_element(), 3)
        self.assertEqual(self.stack.pop_element(), 2)
        self.assertEqual(self.stack.peek_element(), 1)




    def test_that_stack_can_push_element_and_get_the_stack_size(self):
        self.stack.append_element(1)
        self.assertEqual(self.stack.get_size(), 1)



    def test_that_stack_can_push_3_elements_and_get_the_stack_size(self):
        self.stack.append_element(1)
        self.stack.append_element(2)
        self.stack.append_element(3)
        self.assertEqual(self.stack.get_size(), 3)



    def test_that_stack_can_push_3_elements_get_the_stack_size_pop2_elements_get_new_stack_size(self):
        self.stack.append_element(1)
        self.stack.append_element(2)
        self.stack.append_element(3)
        self.assertEqual(self.stack.get_size(), 3)
        self.assertEqual(self.stack.pop_element(), 3)
        self.assertEqual(self.stack.pop_element(), 2)
        self.assertEqual(self.stack.get_size(), 1)


    def test_pop_from_empty_stack(self):
        with self.assertRaises(IndexError):
            self.stack.pop_element()


    def test_peek_on_empty_stack(self):
        with self.assertRaises(IndexError):
            self.stack.peek_element()


    def test_push_none_and_duplicate_values(self):
        self.stack.append_element(None)
        self.assertIsNone(self.stack.peek_element())
        self.stack.append_element(1)
        self.stack.append_element(1)
        self.assertEqual(self.stack.pop_element(), 1)
        self.assertEqual(self.stack.pop_element(), 1)
        self.assertIsNone(self.stack.pop_element())




    def test_check_empty_state_after_multiple_operations(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.append_element(1)
        self.assertFalse(self.stack.is_empty())
        self.stack.pop_element()
        self.assertTrue(self.stack.is_empty())


    def test_size_of_stack_after_operations(self):
        self.assertEqual(self.stack.get_size(), 0)
        self.stack.append_element(1)
        self.assertEqual(self.stack.get_size(), 1)
        self.stack.append_element(2)
        self.assertEqual(self.stack.get_size(), 2)
        self.stack.pop_element()
        self.assertEqual(self.stack.get_size(), 1)
        self.stack.pop_element()
        self.assertEqual(self.stack.get_size(), 0)
























if __name__ == '__main__':
    unittest.main()






# Operations: push (add to top),
# pop (remove from top),
# peek (look at the top without removing),
# is_empty (check if empty)



#Test that stack sizes can not pass
# Test pushing elements to the stack and verify the top element.
# Test popping elements and check the updated top.
# Test checking if the stack is empty after all elements are popped.


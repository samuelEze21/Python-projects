import unittest

import queue


class TestQueue(unittest.TestCase):

    def setUp(self):
        self.queue = queue.Queue()



    def test_that_queue_is_empty_with_no_items(self):
        self.assertTrue(self.queue.is_empty())



    def test_that_element_adds_element_to_queue(self):
        self.queue.enqueue_element(10)
        self.assertEqual(self.queue.peek_element(), 10)
        self.assertEqual(self.queue.size(), 1)



    def test_that_2_elements_can_be_added_and_removed_from_queue(self):
        self.queue.enqueue_element(10)
        self.queue.enqueue_element(15)
        self.queue.dequeue_remove_element()
        self.queue.dequeue_remove_element()
        self.assertEqual(self.queue.size(),0)



    def test_that_2_elements_can_be_be_added_and_1_element_dequed_from_queue(self):
        self.queue.enqueue_element(10)
        self.queue.enqueue_element(18)
        self.queue.dequeue_remove_element()
        self.assertEqual(self.queue.size(),1)



    def test_dequeue_from_empty_queue_raises_error(self):
        with self.assertRaises(IndexError):
                self.queue.dequeue_remove_element()


    def test_that_peek_method_views_the_head_of_the_queue_and_not_remove_elements(self):
        self.queue.enqueue_element(68)
        self.queue.enqueue_element(75)
        self.assertEqual(self.queue.peek_element(), 68)

    def test_enqueue_into_empty_queue(self):
        self.queue.enqueue_element(1)
        self.assertEqual(self.queue.peek_element(), 1)
        self.assertFalse(self.queue.is_empty())


    def test_peek_on_empty_queue(self):
        with self.assertRaises(IndexError):
            self.queue.peek_element()


    def test_dequeue_from_empty_queue(self):
        with self.assertRaises(IndexError):
            self.queue.dequeue_remove_element()


    def test_remove_element_not_in_queue(self):
        self.queue.enqueue_element(1)
        self.queue.enqueue_element(2)
        self.queue.remove_element(3)
        self.assertEqual(self.queue.size(), 2)

    def test_remove_last_element(self):
        self.queue.enqueue_element(1)
        self.queue.dequeue_remove_element()  # Remove the only element
        self.assertTrue(self.queue.is_empty())

    def test_enqueue_and_dequeue_sequence(self):
        self.queue.enqueue_element(1)
        self.queue.enqueue_element(2)
        self.queue.enqueue_element(3)
        self.assertEqual(self.queue.dequeue_remove_element(), 1)  # First in, first out
        self.assertEqual(self.queue.dequeue_remove_element(), 2)
        self.assertEqual(self.queue.dequeue_remove_element(), 3)
        self.assertTrue(self.queue.is_empty())


    def test_multiple_enqueues_and_dequeues(self):
        elements = [1, 2, 3, 4, 5]
        for element in elements:
            self.queue.enqueue_element(element)
        self.assertEqual(self.queue.size(), 5)

        for element in elements:
            self.assertEqual(self.queue.dequeue_remove_element(), element)

        self.assertTrue(self.queue.is_empty())


    def test_front_after_dequeue(self):
        self.queue.enqueue_element(1)
        self.queue.enqueue_element(2)
        self.queue.dequeue_remove_element()  # Remove 1
        self.assertEqual(self.queue.front(), 2)



















if __name__ == '__main__':
    unittest.main()



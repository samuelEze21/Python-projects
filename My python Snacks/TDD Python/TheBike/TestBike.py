import unittest

import bike



class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.bike = bike.Bike(True, 0)

    def test_that_bike_function_exist(self):
        pass

    def test_that_the_bike_can_Be_turn_On(self):
        turn_on_bike = bike.turn_bike_on(self, True)
        self.assertEqual(True, turn_on_bike)


    def test_that_the_bike_can_Be_turn_Off(self):
        turn_off_bike = bike.turn_bike_off(self, True)
        self.assertEqual(True, turn_off_bike)





if __name__ == '__main__':
    unittest.main()

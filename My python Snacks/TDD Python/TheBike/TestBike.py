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


    def test_that_the_bike_can_be_accelerated_by_gear_1(self):
        accelerate_gear1 = bike.accelerate_gear1(self, True, "gear_1", 0)
        self.assertEqual(1, accelerate_gear1)


    def test_that_the_bike_can_be_accelerated_by_gear_2(self):
        accelerate_gear2 = bike.accelerate_gear2(self, True, "gear_2", 21)
        self.assertEqual(23, accelerate_gear2)

    def test_that_the_bike_can_be_accelerated_by_gear_3(self):
        accelerate_gear3 = bike.accelerate_gear3(self, True, "gear_3", 31)
        self.assertEqual(34, accelerate_gear3)


    def test_that_the_bike_can_be_accelerated_by_gear_4(self):
        accelerate_gear4 = bike.accelerate_gear4(self, True, "gear_4", 41)
        self.assertEqual(45, accelerate_gear4)










if __name__ == '__main__':
    unittest.main()

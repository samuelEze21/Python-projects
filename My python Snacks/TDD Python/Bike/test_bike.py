import unittest

from SamuelPythonProjects.Bike import bike


class TestBike(unittest.TestCase):

    def setUp(self):
        self.bike = bike.Bike()



    def test_bike_can_be_turned_on(self):
        turn_on = self.bike.turn_bike_on()
        self.assertTrue(turn_on, "Bike is On")


    def test_bike_can_be_turned_off(self):
        turn_off = self.bike.turn_bike_off()
        self.assertEqual(turn_off, True)


    def test_that_the_bike_can_be_accelerated_by_gear1(self):
        self.bike.turn_bike_on()
        starting_speed = self.bike.bike_speed = 15
        accelerate_gear1 = self.bike.accelerate_gear_levels(1)
        self.assertEqual(accelerate_gear1, 16)



    def test_that_the_bike_can_be_accelerated_by_gear2(self):
        self.bike.turn_bike_on()
        self.bike.bike_speed = 22
        accelerate_gear2 = self.bike.accelerate_gear_levels(2)
        self.assertEqual(accelerate_gear2, 24)



    def test_that_the_bike_can_be_accelerated_by_gear3(self):
        self.bike.turn_bike_on()
        self.bike.bike_speed = 34
        accelerate_gear3 = self.bike.accelerate_gear_levels(3)
        self.assertEqual(accelerate_gear3, 37)



    def test_that_the_bike_can_be_accelerated_by_gear4(self):
        self.bike.turn_bike_on()
        self.bike.bike_speed = 40
        accelerate_gear4 = self.bike.accelerate_gear_levels(4)
        self.assertEqual(accelerate_gear4, 44)



    def test_that_bike_can_be_decelerated_by_gear1(self):
        self.bike.turn_bike_on()
        self.bike.bike_speed = 18
        decelerate_gear1 = self.bike.decelerate_gear_levels(1)
        self.assertEqual(decelerate_gear1, 17)


    def test_that_bike_can_be_decelerated_by_gear2(self):
        self.bike.turn_bike_on()
        self.bike.bike_speed = 24
        decelerate_gear2 = self.bike.decelerate_gear_levels(2)
        self.assertEqual(decelerate_gear2, 22)


    def test_that_bike_can_be_decelerated_by_gear3(self):
        self.bike.turn_bike_on()
        self.bike.bike_speed = 34
        decelerate_gear3 = self.bike.decelerate_gear_levels(3)
        self.assertEqual(decelerate_gear3, 31)


    def test_that_bike_can_be_decelerated_by_gear4(self):
        self.bike.turn_bike_on()
        self.bike.bike_speed = 44
        decelerate_gear4 = self.bike.decelerate_gear_levels(4)
        self.assertEqual(decelerate_gear4, 40)




    # def test that bike can not be turned on, if ignition_is_on != True;
    # def test that bike can not go above or below speed limit for gear ranges
    # def test that bike can accelerate and decelerate automatically
    # def test that gear speed are in the given ranges















if __name__ == '__main__':
    unittest.main()

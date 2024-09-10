import unittest

from unittest import TestCase

import airconditional
from AC.airconditional import increase_temperature


class MyTestCase(unittest.TestCase):


    def test_that_Ac_is_Turned_On(self):

        ac_on = airconditional.turn_on_ac(True, temperature = 24)
        self.assertTrue(ac_on)



    def test_that_Ac_is_Turned_Off(self):

        ac_off = airconditional.turn_off_ac(False, temperature = 0)
        self.assertFalse(ac_off)



    def test_that_Ac_is_On_WhenI_IncreaseTemperature_CoolingReduces(self):

        ac_on = True

        ac_high_temp_low_cooling = airconditional.increase_temperature(30, decrease_cooling = True)
        self.assertTrue(ac_high_temp_low_cooling)


    def test_that_Ac_Is_on_When_I_decreaseTemperature_CoolingIncreases(self):
        ac_on = True

        ac_decreased_temp_high_cooling = airconditional.decrease_temperature(16, increase_cooling = True)
        self.assertTrue(ac_decreased_temp_high_cooling)



    def test_thatWhen_Ac_is_On_and_Temperature_increases_above_30(self):
        ac_on = True

        increase_temperature_above_thirty = airconditional.increase_temperature(31, "The Temperature can not exceed 30")
        self.assertTrue(increase_temperature_above_thirty)












    # def test_something(self):
       # self.assertEqual(True, False)  # add assertion here


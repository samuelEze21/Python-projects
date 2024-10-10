import unittest

from tv import Tv

class TestTv(unittest.TestCase):

    def setUp(self):
        self.tv1 = Tv()

    def test_that_new_Tv_can_be_turned_on(self):
        self.assertFalse(self.tv1.get_is_on())
        self.tv1.turn_tv_on()
        self.assertTrue(self.tv1.get_is_on())


    def test_that_Tv_can_be_turned_off(self):
        self.tv1.turn_tv_on()
        self.assertTrue(self.tv1.get_is_on())
        self.tv1.turn_tv_off()
        self.assertFalse(self.tv1.get_is_on())


    def test_that_tv_channel_can_be_gotten(self):
        self.tv1.turn_tv_on()
        self.assertTrue(self.tv1.get_is_on())
        get_channel = self.tv1.get_tv_channel(88)
        self.assertEqual(self.tv1.get_tv_channel(88), get_channel)


    def test_that_tv_channel_can_be_set(self):
        self.tv1.turn_tv_on()
        self.assertTrue(self.tv1.get_is_on())
        current_channel = self.tv1.get_tv_channel(1)
        self.assertEqual(self.tv1.get_tv_channel(1), current_channel)
        set_channel = self.tv1.set_tv_channel(4)
        self.assertEqual(self.tv1.get_tv_channel(4), set_channel)



    def test_that_volume_can_be_gotten(self):
        self.tv1.turn_tv_on()
        self.assertTrue(self.tv1.get_is_on())
        get_volume = self.tv1.get_tv_volume(8)
        self.assertEqual(self.tv1.get_tv_volume(8), get_volume)



    def test_that_volume_can_be_set(self):
        self.tv1.turn_tv_on()
        self.assertTrue(self.tv1.get_is_on())
        current_volume = self.tv1.get_tv_volume(8)
        self.assertEqual(self.tv1.get_tv_volume(8), current_volume)
        set_volume = self.tv1.set_tv_volume(9)
        self.assertEqual(self.tv1.set_tv_volume(9), set_volume)



    def test_that_channel_can_go_up(self):
        self.tv1.turn_tv_on()
        self.assertTrue(self.tv1.get_is_on())
        current_channel = self.tv1.get_tv_channel(90)
        self.assertEqual(self.tv1.get_tv_channel(90), current_channel)

        self.tv1.set_tv_channel_up(90)
        channel_up = self.tv1.get_tv_channel(91)
        self.assertEqual(channel_up, 91)



    def test_that_channel_can_go_down(self):
        self.tv1.turn_tv_on()
        self.assertTrue(self.tv1.get_is_on())
        current_channel = self.tv1.get_tv_channel(55)










        # channel_up = self.tv1.get_tv_channel(89)
        # self.assertEqual(self.tv1.set_tv_channel_up(89), channel_up)
        #
        #
        # self.tv1.set_tv_channel_up(90)  # Increase the channel from 90 to 91
        # channel_up = self.tv1.get_tv_channel()
        # self.assertEqual(channel_up, 91)


 # def test_channel_up_from_98_to_99(self):
 #        # Test that channel goes from 98 to 99 when incremented
 #        new_channel = self.tv.set_tv_channel_up(self.tv.channel)
 #        self.assertEqual(new_channel, 99)
 #











#
#
#     def test_that_tv_channel_can_be_gotten(self):
#         get_channel = tv.get_tv_channel(self,True, 100)
#         self.assertEqual(100, get_channel)
#
#
#     def test_that_tv_channel_can_be_set(self):
#         set_channel = tv.set_tv_channel(self,True, 24)
#         self.assertEqual(24, set_channel)
#
#
#     def test_that_tv_volume_can_be_gotten(self):
#         get_volume = tv.get_tv_volume(self,True, 9)
#         self.assertEqual(9, get_volume)
#
#
#     def test_that_tv_volume_can_be_set(self):
#         set_volume = tv.set_tv_volume(self,True, 10)
#         self.assertEqual(10, set_volume)
#
#
#
#
#
#
# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(True, False)  # add assertion here
#
#
# if __name__ == '__main__':
#     unittest.main()

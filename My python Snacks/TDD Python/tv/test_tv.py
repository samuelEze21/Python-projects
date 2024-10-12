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



    def test_that_tv_volume_can_be_gotten(self):
        self.tv1.turn_tv_on()
        self.assertTrue(self.tv1.get_is_on())
        get_volume = self.tv1.get_tv_volume(8)
        self.assertEqual(self.tv1.get_tv_volume(8), get_volume)



    def test_that_tv_volume_can_be_set(self):
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
        current_channel = self.tv1.get_tv_channel(55)
        self.assertEqual(self.tv1.get_tv_channel(55), current_channel)
        self.tv1.set_tv_channel_down(54)
        channel_down = self.tv1.get_tv_channel(54)
        self.assertEqual(channel_down, 54)



    def test_that_volume_can_go_up(self):
        self.tv1.turn_tv_on()
        self.assertTrue(self.tv1.get_is_on())
        current_volume = self.tv1.get_tv_volume(9)
        self.assertEqual(self.tv1.get_tv_volume(9), current_volume)
        self.tv1.set_tv_volume_up(9)
        self.assertEqual(self.tv1.set_tv_volume_up(9), 10)


    def test_that_volume_can_go_down(self):
        self.tv1.turn_tv_on()
        self.assertTrue(self.tv1.get_is_on())
        current_volume = self.tv1.get_tv_volume(5)
        self.assertEqual(self.tv1.get_tv_volume(5), current_volume)
        self.tv1.set_tv_volume_down(5)
        self.assertEqual(self.tv1.set_tv_volume_down(5), 4)



    def test_that_volume_can_be_muted(self):
        self.tv1.turn_tv_on()
        self.assertTrue(self.tv1.get_is_on())
        current_volume = self.tv1.get_tv_volume(9)
        self.assertEqual(self.tv1.get_tv_volume(9), current_volume)
        self.tv1.mute_tv_volume(9)
        self.assertEqual(self.tv1.mute_tv_volume(9), 0)



    def test_that_volume_can_be_un_muted(self):
        self.tv1.turn_tv_on()
        self.assertTrue(self.tv1.get_is_on())
        self.tv1.mute_tv_volume(7)
        self.assertEqual(self.tv1.mute_tv_volume(7), 0)
        self.tv1.unmute_tv_volume(7)
        self.assertEqual(self.tv1.unmute_tv_volume(7), 7)












if __name__ == '__main__':
    unittest.main()

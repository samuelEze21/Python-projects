import unittest

import pizzawahala



class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.pizzawahala = pizzawahala.PizzaWahala(0, "select_pizza_type")


    def test_that_pizzawahala_function_exists(self):
        pass


    def test_that_pizza_has_four_types_and_has_exact_number_of_slices(self):
        pizza1 = pizzawahala.get_pizza_types(self, "sapa_size", 4)
        self.assertTrue(4, pizza1)
        pizza2 = pizzawahala.get_pizza_types(self, "small_money", 6)
        self.assertTrue(6, pizza2)
        pizza3 = pizzawahala.get_pizza_types(self, "big_boys", 8)
        self.assertTrue(8, pizza3)
        pizza4 = pizzawahala.get_pizza_types(self, "odogwu", 12)
        self.assertTrue(12, pizza4)


    def test_that_prices_for_pizza_is_set_according_to_types_of_pizza(self):
        pizza1 = pizzawahala.get_price_for_pizza( self, 2000, "sapa_size")
        self.assertTrue(2000, pizza1)
        pizza2 = pizzawahala.get_price_for_pizza(self, 2400, "small_money")
        self.assertTrue(2400, pizza2)
        pizza3 = pizzawahala.get_price_for_pizza(self, 3000, "big_boys")
        self.assertTrue(3000, pizza3)
        pizza4 = pizzawahala.get_price_for_pizza(self,  4200, "odogwu")
        self.assertTrue(4200, pizza4)


    def test_for_when_user_Put_in_invalid_pizza_type(self):
        invalid_pizza_type = pizzawahala.get_pizza_types(self, "sofine_Pizza", 55)
        self.assertFalse(invalid_pizza_type)


    def test_for_how_many_boxes_needed_for_the_party_ifNumber_ofGuest_is_known_And_pizza_type_is_known(self):
        total_boxes_needed = pizzawahala.get_number_of_pizza_boxes_user_to_purchase(self,44, "big_boys")
        self.assertEqual(6, total_boxes_needed)
        total_boxes_2nd_customer = pizzawahala.get_number_of_pizza_boxes_user_to_purchase(self, 48, "sapa_size")
        self.assertEqual(12, total_boxes_2nd_customer)




    # test with edge cases, such as zero guests or a negative number of slices.












if __name__ == '__main__':
    unittest.main()

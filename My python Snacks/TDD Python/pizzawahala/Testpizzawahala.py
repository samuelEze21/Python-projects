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
        total_boxes_needed = pizzawahala.get_number_of_pizza_boxes_user_have_to_purchase(self,44, "big_boys")
        self.assertEqual(6, total_boxes_needed)
        total_boxes_2nd_customer = pizzawahala.get_number_of_pizza_boxes_user_have_to_purchase(self, 50, "sapa_size")
        self.assertEqual(13, total_boxes_2nd_customer)
        total_boxes_3rd_customer = pizzawahala.get_number_of_pizza_boxes_user_have_to_purchase(self, 84, "small_money")
        self.assertEqual(14, total_boxes_3rd_customer)
        total_boxes_4th_customer = pizzawahala.get_number_of_pizza_boxes_user_have_to_purchase(self, 100, "odogwu")
        self.assertEqual(9, total_boxes_4th_customer)


    def test_for_how_many_slices_to_be_left_over(self):
        left_over_slices = pizzawahala.get_left_over_slices(self, 45, 6, "big_boys")
        self.assertEqual(3, left_over_slices)
        left_over_slices2 = pizzawahala.get_left_over_slices(self, 34, 9, "sapa_size")
        self.assertEqual(2, left_over_slices2)
        left_over_slices3 = pizzawahala.get_left_over_slices(self,68, 12, "small_money")
        self.assertEqual(4, left_over_slices3)
        left_over_slices4 = pizzawahala.get_left_over_slices(self,33, 3, "odogwu")
        self.assertEqual(3, left_over_slices4)


    def test_for_totalCost_UserHasToPay_for_pizzaType_AndNumber_OfBoxesPurchased(self):
        total_pizza_cost = pizzawahala.get_total_cost_pizza_boxes_pur(self, "sapa_size", 2000, 7)
        self.assertEqual(14000, total_pizza_cost)
        total_pizza_cost_pizza2 = pizzawahala.get_total_cost_pizza_boxes_pur(self, "small_money", 2400, 11)
        self.assertEqual(26400, total_pizza_cost_pizza2)
        total_pizza_cost_pizza3 = pizzawahala.get_total_cost_pizza_boxes_pur(self, "big_boys", 3000, 8)
        self.assertEqual(24000, total_pizza_cost_pizza3)
        total_pizza_cost_pizza4 = pizzawahala.get_total_cost_pizza_boxes_pur(self, "odogwu", 4200, 5)
        self.assertEqual(21000, total_pizza_cost_pizza4)




    # def test_that_when_customer_is_prompted_for_input_only_valid_data_types_are_supplied(self):
    # test for when prompt brings back zero_negative(invalid guests) or a negative number of boxes needed(self):












if __name__ == '__main__':
    unittest.main()

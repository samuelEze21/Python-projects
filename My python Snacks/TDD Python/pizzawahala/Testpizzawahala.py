import unittest

import pizzawahala



class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.pizzawahala = pizzawahala.PizzaWahala(50, "sapa_size")


    def test_that_pizzawahala_function_exists(self):
        pass


    def test_that_pizza_has_four_types_and_exact_has_slices(self):
        #self.pizza = Pizzawahala()
        pizza1 = pizzawahala.get_pizza_types(self, "sapa_size", 4)
        self.assertTrue(4, pizza1)
        pizza2 = pizzawahala.get_pizza_types(self, "small_money", 6)
        self.assertTrue(6, pizza2)
        pizza3 = pizzawahala.get_pizza_types(self, "big_boys", 8)
        self.assertTrue(8, pizza3)
        pizza4 = pizzawahala.get_pizza_types(self, "odogwu", 12)
        self.assertTrue(12, pizza4)


    def test_that_prices_for_pizza_is_set_according_to_types_of_pizza(self):
        pizza1 = pizzawahala.get_price_for_pizza( self, "sapa_size", 2000)
        self.assertTrue(2000, pizza1)
        pizza2 = pizzawahala.get_price_for_pizza(self, 2400, "small_money")
        self.assertTrue(2400, pizza2)
        pizza3 = pizzawahala.get_price_for_pizza(self, 3000, "big_boys")
        self.assertTrue(3000, pizza3)
        pizza4 = pizzawahala.get_price_for_pizza(self,  4200, "odogwu")
        self.assertTrue(4200, pizza4)


    #def test_that_if_each_Consumer_is_to_consume_1PizzaEach_With_The_Number_of_Guests_and_pizzaTypeKnown_number_Of_PizzaBoxes_needed_can_be_calculated(self):














if __name__ == '__main__':
    unittest.main()

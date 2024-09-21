class PizzaWahala:

    def __init__(self, number_of_guests, pizza_type):
        self.number_of_guests = number_of_guests
        self.pizza_type = pizza_type #use list to display pizza-types and lists (key/value pair)




def get_pizza_types(self, pizza_type, number_of_slices):
    if pizza_type == "sapa_size":
        self.number_of_slices = 4

    elif pizza_type == "small_money":
        self.number_of_slices = 6

    elif pizza_type == "big_boys":
        self.number_of_slices = 8

    elif pizza_type == "odogwu":
        self.number_of_slices = 12

        return self.number_of_slices
    else:
        print("This pizza type is not available")




def get_price_for_pizza(self, price_per_box, pizza_type):
    if pizza_type == "sapa_size":
        self.price_per_box = 2000

    elif pizza_type == "small_money":
        self.price_per_box = 2400

    elif pizza_type == "big_boys":
         self.price_per_box = 3000

    elif pizza_type == "odogwu":
        self.price_per_box = 1800

    return self.price_per_box



def get_number_of_pizza_boxes_user_to_purchase(self, number_of_guests, pizza_type):
    number_of_slices = {
        "sapa_size": 4,
        "small_money": 6,
        "big_boys": 8,
        "odogwu": 12
    }

    slices_per_box = number_of_slices.get(pizza_type, None)
    if slices_per_box is None:
        return "Invalid pizza type."


    self.total_boxes = number_of_guests // slices_per_box
    if number_of_guests % slices_per_box != 0:
        self.total_boxes += 1

    return self.total_boxes


def my_discount(price, discount):
    discount_amount = (discount / 100) * price

    final_price = price - discount_amount
    return final_price

price_after_discount = my_discount(150, 15)

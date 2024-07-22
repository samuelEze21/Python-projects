carprice = int(input("Enter the price of your car: "))

less_than_million = carprice / 100 * 10
over_million_and_three_million = carprice / 100 * 15
over_three_and_five_million = carprice / 100 * 20
over_five_million = carprice / 100 * 25

if carprice <= 1000000:
    print("Your car road tax is", less_than_million)
elif carprice <= 3000000:
    print("Your car road tax is", over_million_and_three_million)
elif carprice <= 5000000:
    print("Your car road tax is", over_three_and_five_million)
else:
    print("Your car road tax is", over_five_million)







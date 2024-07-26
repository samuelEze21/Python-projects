One_foot = 0.305

#collect a number input in ft
number_foot = int(input("Enter a Number in foot: ")) 

#converting collected input from feet to meter
number_meter = 0.305 * number_foot

#casting, to ensure output gets printed in float
number_meter = float(number_meter) 

#printing meter result
print("Your meter for your foot input is", number_meter)

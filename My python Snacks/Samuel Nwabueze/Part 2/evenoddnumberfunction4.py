def even_odd_integer(number):
	if number % 2 == 0:
		number += even_number
		return even_number 

	else: 
		number += odd_number
		return odd_number


number = 42

if(number % 2 == 0): 
	print(number, "is even") 

else: 
	print(number, "is odd") 








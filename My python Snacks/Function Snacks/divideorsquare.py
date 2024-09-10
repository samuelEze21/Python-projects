import math 
def divide_or_square(number): 
	
	if number % 5 == 0: 
		squareroot = math.sqrt(number)
		return f"{squareroot}"
	elif number % 5 > 0: 
		remainder = number % 5 
		return f"{remainder}" 

print(divide_or_square(10))
		
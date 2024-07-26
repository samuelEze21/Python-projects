#collect a number between 0 and 1000
number = int(input('Enter a number between 0 and 1000: "))

#assign variable to the sum and use while to check that the numbers (0 -10 are extracted))
sum_number = 0
	while (number != 0): 
		sum_number = sum_number + (number % 10)
		number = number // 10  
		
		#print sum result
		print("sum of your numbers added is", sum_number) 


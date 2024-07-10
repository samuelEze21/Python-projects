number1 = input("enter first number: ") 
number2 = input("enter second number: ") 
number3 = input("enter third number: ") 

number1 = int (number1) 
number2 = int (number2) 
number3 = int (number3) 

sum = number1 + number2 + number3
print("sum =", sum)

average = sum / 3
print("average =", average)

product = number1 * number2 * number3
print("product =", product)


if number1 > number2 and number3:
	print("number1 is the greatest number")

elif number2 > number1 and number3: 
	print("number2 is the greatest number")

elif number3 > number1 and number2: 
	print("number3 is the greatest number")


if number1 < number2 and number3:
	print("number1 is the smallest number")

elif number2 < number1 and number3: 
	print("number2 is the smallest number")

elif number3 < number1 and number2: 
	print("number3 is the smallest number")





def get_sortedNumbers(num1, num2, num3):
	if num1 > num2 and num3:
		return num1, num2, num3 
	if num2 > num1 and num3:
		return num2, num1, num3

	if num3 > num1 and num2:
		return num3, num1, num2



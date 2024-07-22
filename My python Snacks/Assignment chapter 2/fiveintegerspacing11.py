numbers = []


for five_digits in range(1, 6): 
	number = int(input("Enter 5 numbers of your choice: "))
	numbers.append(number) 


print("Your Inputed Five integers are: ", end="")
for number in numbers:
    print(number, end="   ")
print()


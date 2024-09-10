passcounter = 0
failcounter = 0

for grades in range(1, 16):
	score = int(input(f"Enter score for student {grades}: "))

	if score >= 45:
		print("You passed this exam")
		passcounter += 1
	
	else:
		print("You have failed this exam") 
		failcounter += 1

print(f"The number of passed students are: {passcounter}") 
print(f"The number of failed students are: {failcounter}") 


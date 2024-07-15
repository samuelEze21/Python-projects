passscore = 0
failscore = 0


for countergradescore in range(1, 11): 
	gradescore = int(input("Enter your score for student {}: 1 for pass, 2 for fail: ".format(countergradescore)))
	

	while gradescore != 1 and gradescore != 2:
		gradescore = int(input("Invalid input. Enter 1 for pass or 2 for fail: "))


	if gradescore == 1:
        	passscore += 1
        	print("Passed student count: ", passscore)

	if gradescore == 2: 
        	failscore += 1
        	print("Failed student count: ", failscore)

print("The total number of pass mark is: ", passscore)
print("The total number of failures is: ", failscore)



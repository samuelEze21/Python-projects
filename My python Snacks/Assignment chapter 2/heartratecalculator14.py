age = int(input( "enter your age: ")) 

maximum_heart_rate = 220 - int(age) 

target_heart_rate = maximum_heart_rate / 100 

for target_heart_rate in range(50, 86): 
	if target_heart_rate == 50 and target_heart_rate <= 86: 
		print(f"Your maximum heart rate is", maximum_heart_rate) 
		print(f"The range of your target heart rate is", {target_heart_rate}) 

print()



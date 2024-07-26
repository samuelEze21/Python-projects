year = 525600 
day = 1440 

#Ask the user to enter the number of minutes
number_minutes = int(input("Enter number of minutes you want: "))

#convert the number of minutes to year by using the formular declared for year
number_years = number_minutes / year

if number_minutes / year != 0: 
	number_days = number_minutes % year
	number_days = float(number_days)

#print number of years and days resulting 
print(f"Your number in years is", {number_years}, 'years'  " and", {number_days}, 'days')

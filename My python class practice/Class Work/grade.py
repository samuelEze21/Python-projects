grade = input("enter your grade: ")

grade = int (grade) 


if grade >= 75 and grade == 100:
	print("your score is A, Excellent student") 

if grade >= 65 and grade <= 74:
	print("your score is B, Bravo!") 

if grade >= 50 and grade <= 64:
	print("your score is C, You can do better") 

if grade >= 40 and grade <= 49:
	print("your score is D, Try Harder") 

if grade >= 101:
	print("Thief! invalid score") 

if grade <= 39:
	print("your score is F, Just drop out sir!") 




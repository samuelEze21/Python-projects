problem = input("What is your problem?: ") 

problem_followup = input("Have you had this problem before (yes or no)? ").strip().lower()

if problem_followup == "yes": 
	print("Well, you have it again") 
	
else:
	print('Well, you have it now')



#Would this conversation convince the user that the entity at the other end exhibited intelligent behavior? 
#I think it does to some extent in making the user think the response was as a result of the communication that happened prior 


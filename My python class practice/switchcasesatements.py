language = input("enter your preferred language: ") 

match language: 

	case "java": 
		print("you are a java programmer") 
	case "python": 
		print("you are a python programmer") 
	case _: 
		print("you are a software engineer") 



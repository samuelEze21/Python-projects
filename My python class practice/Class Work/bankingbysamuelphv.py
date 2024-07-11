stop = 1
balance = 0

print("Hello, Welcome to PHV bank by Samuel Limited, How can we help yoy Today?: ")
 

while stop != 0: 

	
	transaction = int(input("enter 1 to deposit or 2 to withdraw or 3 to see balance: "))

	if transaction == 1:

			deposit = int (input("enter deposit amount:"))
			balance += deposit 
			
	if transaction == 2:
			withdrawal = int (input("enter withdrawal amount:"))
			balance -= withdrawal

	if transaction == 3: 
			print( " Your Net availabe balance is: ", balance )

	stop = ("enter 0 to stop or 1 to continue to the Main Bank Menu: ") 

print( " Your Net availabe balance is: ", balance )



import random

count = 0
guess_again = 0

number = random.randint(1, 10) 

while guess_again != 1:

	answer = int(input(" Guess my number between 1 and 1000 with the fewest guesses: "))
	count +=1

	if answer > number :
		print( "too high, You can try again, guess my number between 1 and 1000 with the fewest guesses: ")

	elif answer < number:
		print( "too low, You can try again, guess my number between 1 and 1000 with the fewest guesses: ")

	elif answer == number:
		if count <= 50: 
			print(f"Congratulations. You guessed the number in {count} times!")

		elif count <= 50: 
			print(f"Congratulations. You guessed the number in {count} times!, you can try to play again")
		number = random.randint(1, 10) 

		guess_again = int(input(" Do you wanna play again?, press 1 to stop, and 2 to play: "))
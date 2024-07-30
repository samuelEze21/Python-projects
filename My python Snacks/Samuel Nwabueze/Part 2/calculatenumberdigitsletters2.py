#define all digits as string
natural_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
 
# define all possible letters to be inputted
all_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 
			't', 'u', 'v', 'w', 'x', 'y', 'z']

 
# collecting letters and digits inputs and storing to string_input 
string_input = input("Enter Your Letters and digits: ")
 

# storing values of digits and letters
total_digits = 0
total_letters = 0
 

# forloop to iterate across user inputs

for sentence in string_input:
 
	if sentence in natural_digits:
		total_digits += 1
 
	elif sentence in all_letters:
        	total_letters += 1

#printing total letters and digits found
print("Total letters found:", total_letters)
print("Total digits found:", total_digits)




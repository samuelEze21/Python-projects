#collect inputs for subtotal amount
sub_total = int(input("Enter your subtotal amount: ")) 

#collect input for the gratuity rate
gratuity_amount = int(input("Enter your gratuity rate(%): ")) 


#compute the gratuity rate by converting the gratuity amount to a percentage and multiply by subtotal amount 
gratuity_rate = gratuity_amount / 100 * sub_total

#cast gratuityrate to floatingnumber
gratuity_rate = float (gratuity_rate) 

#calculate totalamount by adding subtotal + gratuityrate
total_amout = sub_total + gratuity_rate

#casting to float for the totalamount to fit the data type
total_amout = float(total_amout) 

#print gratuityrate and totalamount
print("Your gratuity is", gratuity_rate)
print("Your total amount is", total_amout)

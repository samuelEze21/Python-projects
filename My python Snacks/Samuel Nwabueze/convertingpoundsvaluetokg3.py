#formula given
One_pound = 0.454


#collect a number input in pound
pound_value = int(input("Enter a pound value: ")) 

#converting collected value from pounds to KG
kilograme_value = 0.454 * pound_value

#casting, to ensure output gets printed in float
kilograme_value = float (kilograme_value) 

#result printed in Kg
print("Your KG for your pound entry is", kilograme_value)

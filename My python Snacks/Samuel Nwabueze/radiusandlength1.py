π = 3.14159

#collect radius of cylinder from user 
cylinder_radius = int(input("Enter your radius")) 

#collect length of cylinder from user 
cylinder_length = int(input("Enter your length")) 

#using the given area formula
cylinder_area = π * cylinder_radius ** cylinder_radius

#using the given volume formula
cylinder_volume = cylinder_area * cylinder_length

#casting the expected result to float 
cylinder_area = float (cylinder_area) 
cylinder_volume = float (cylinder_volume) 

#printing result for area and volume	
print(f"Your cylinder area is", cylinder_area) 
print(f"Your cylinder volume is", cylinder_volume) 

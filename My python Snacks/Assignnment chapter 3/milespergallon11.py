total_miles = 0
total_gallons = 0

sentinel = -1

while True:
    miles = float(input("Enter miles driven (-1 to quit): "))
    if miles == sentinel:
        break
    gallons = float(input("Enter gallons used: "))
    
    mpg = miles / gallons
    print(f"Miles per gallon for this tankful: {mpg:.2f}")
    
    total_miles += miles
    total_gallons += gallons

if total_gallons != 0:
    combined_mpg = total_miles / total_gallons
    print(f"\nCombined miles per gallon for all tankfuls: {combined_mpg:.2f}")
else:
    print("No data to calculate combined miles per gallon.")



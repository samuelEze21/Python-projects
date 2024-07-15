integers = []
num_of_integers = 4

for count in range(num_of_integers):
    integer = int(input(f"Enter integer {count + 1}: "))
    integers.append(integer)

sum_of_integers = sum(integers)
average = sum_of_integers / num_of_integers
product = 1
for integer in integers:
    product *= integer

smallest = min(integers)
largest = max(integers)

print("Sum =", sum_of_integers)
print("Average =", average)
print("Product =", product)
print("Smallest =", smallest)
print("Largest =", largest)

print("a\tb\ta**b")

for number in range(6):
	a = number ** 2
	for number in range(2,7):

	b = number ** 3
	print("{:>6}\t{:>6}\t{:>6}".format(a, b, a**b))

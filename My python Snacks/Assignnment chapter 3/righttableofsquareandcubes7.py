print("Number\tSquare\tCube")

for number in range(6):
    square = number ** 2
    cube = number ** 3
    print("{:>6}\t{:>6}\t{:>6}".format(number, square, cube))

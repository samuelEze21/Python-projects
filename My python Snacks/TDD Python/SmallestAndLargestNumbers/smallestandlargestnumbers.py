def biggest_number(numbers_list):
    numbers_list = [2,3,6,7,8]

    for number in numbers_list:
        if int (number) == max(numbers_list):
            return number


def smallest_number(numbers):
    numbers_list = [2,3,6,7,8]
    for number in numbers_list:
        if int (number) == min(numbers_list):
            return number



def biggest_smallest_numbers(numbers):
    numbers = []
    minimum = numbers[0]
    largest_number = minimum

    for number in numbers:
        if number < minimum:
            minimum = number
            if number > largest_number:
                largest_number = number

    numbers.append(minimum)(largest_number)
    return numbers

print(smallest_number2([2,3,6,7,8]))

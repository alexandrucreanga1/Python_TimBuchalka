even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9, 1, 1, 1]

numbers = [even, odd] #nested list!!!!
print(numbers)

for number_list in numbers:
    print(number_list)

    for value in number_list:
        print(value)


#         01234567890123   <<< indexes
parrot = "Norwegian Blue"

print(parrot[0:6:2])  # Nre >> Start with index 0 upt to index 6 (excluded) in steps of 2
print(parrot[0:6:3])  # Nw  >> Start with index 0 upt to index 6 (excluded) in steps of 3


#number = "9,223;372:036 854,775;807"
number = input("PLease enter a series of numbers, using any separators you like: ")
print(number[1::4])  #>> ,,,,,, starting with 1 and print every 4 step.

separators = ""
for char in number:
    if not char.isnumeric():
        separators = separators + char

print(separators)


values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])
print("Sum is : ",sum([int(val) for val in values]))
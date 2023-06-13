

#         01234567890123   <<< indexes
parrot = "Norwegian Blue"

print(parrot[0:6:2])  # Nre >> Start with index 0 upt to index 6 (excluded) in steps of 2
print(parrot[0:6:3])  # Nw  >> Start with index 0 upt to index 6 (excluded) in steps of 3


number = "9,223,372,036,854,775,807"
print(number[1::4])  #>> ,,,,,, starting with 1 and print every 4 step.

separators = number[1::4]
print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])



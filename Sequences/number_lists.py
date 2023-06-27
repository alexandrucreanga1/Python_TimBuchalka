even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9, 1, 1, 1]

print(min(even))
print(max(even))
print(min(odd))
print(max(odd))

print()
print(len(even))
print(len(odd))

print()
print(odd.count(3))

even.extend(odd)
print(even)
another_even = even
print(another_even)

even.sort(reverse=False)
print(even)
print(another_even)

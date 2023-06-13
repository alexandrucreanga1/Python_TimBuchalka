#          01234567890123456789012345
letters = "abcdefghijklmnopqrstuvwxyz"

print(len(letters))
backwards = letters[26:0:-1]
print(backwards)
backwards = letters[26::-1]
print(backwards)
backwards = letters[::-1]
print(backwards)


# Create slice that produces the characters "qpo"
task1 = letters[letters.index("q"):letters.index("o")-1:-1]
print(task1)
task1v2 = letters[16:13:-1]
print(task1v2)

# create a slice that produce "edcba"
task2 = letters[letters.index("e")::-1]
print(task2)
task2v2 = letters[4::-1]
print(task2v2)


# slice the string to produce the last 8 characters, in reverse order.
task3 = letters[len(letters):len(letters)-9:-1]
print(task3)
print(len(task3))
task3v2 = letters[:-9:-1]
print(task3v2)

print(letters[-4:]) # obtain last 4 letters
print(letters[-1]) # obtain last letter
print(letters[:1]) # obtain first letter
print(letters[0])




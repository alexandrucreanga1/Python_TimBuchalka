name = input("Please enter your name: ")
age = int(input("How old are you, {0}? ".format(name)))
age2 = int(input("How old are you again " + name + "? "))
print(age)
print(age2)

if age >= 18 :
    print("You are old enough to vote!")
else:
    print("You are too young {0} !".format(name))
    print("Please come back in {0} years".format(18-age))

if age <18 :
    print("Please come back in {0}".format(18 - age))
elif age==900 :
    print("Sorry, Yoda, you die in Return of Jedi")
else:
    print("You are are old enough to vote")
    print("Please put an x in the box")
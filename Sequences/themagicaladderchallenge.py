

a,b,c = (input("please enter your three numbers: ").split(","))


#print("entered numbers are: ",a,b,c)
# print(int(a)+int(b)-int(c))


if int(a) or int(b) or int(c) :
    print(int(a)+int(b)-int(c))
else:
    a,b,c = (input("Enter only numbers: ").split(","))
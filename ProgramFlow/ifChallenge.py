yourName = input("Please enter your name: ")
yourAge = int(input ("Please enter your age: "))

maxthreshold = 18
minthreshold = 31

if yourAge >= maxthreshold and yourAge <= minthreshold :
    print("{} you are welcome to the holliday !".format(yourName))
else:
    print("{}, your age, which is {} is out of range of 18-30 to be allowed to this holliday".format(yourName,yourAge))

import random

answer = random.randint(1,10)

print("PLease guess number between 1 and 10: ")
guess = int(input())

if guess < answer :
    print("Please guess higher !")
    print("Correct number is: " + str(answer))
elif guess > answer :
    print("Please guess lower !")
    print("Correct number is: " + str(answer))
else :
    print("You got it first time !")
    print("Correct number is: " + str(answer))
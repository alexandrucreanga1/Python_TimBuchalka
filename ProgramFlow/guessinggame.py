import random

answer = random.randint(1,10)

print("PLease guess number between 1 and 10: ")
guess = int(input())

if guess < answer :
    print("Please guess higher !")
    print("Correct number is: " + str(answer))
    guess = int(input())
    if guess == answer:
        print("well done, you guessed it")
    else:
        print("Sorry wrong number at this time")
elif guess > answer :
    print("Please guess lower !")
    print("Correct number is: " + str(answer))
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it")
    else:
        print("sorry, wrong number at this time")
else :
    print("You got it first time !")
    print("Correct number is: " + str(answer))
import random

highest = 20
answer = random.randint(1, highest)
print(answer)


player_input = 0
print(("Please enter your number to be checked between 1 and {}: ").format(highest))

while player_input != answer :
    player_input = int(input())

    if player_input == 0 :
        print("Game over by player!")
        break
    if player_input == answer:
        print("you got it first time")
        print("well done , you guess it")
        break

    else:
        if player_input < answer :
            print("Wrong answer, guess a higher number")
        else:
            print("Wrong answer, guess a lower number")





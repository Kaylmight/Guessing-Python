import random

number = random.randint(0, 20)
chances = 0

while chances < 5:
    guess = int(input("Guess the number: "))
    if guess > number:
        print("The guess is higher than the actual number")

    elif guess < number:
        print("The guess is lower than the actual number")

    else:
        print("You have successfully guessed the number, Congratulations!")
        break

    chances = chances + 1

if not chances < 5:
    print("Unfortunately you have used all your lives, the number was", number)
from random import *

points = 10
value = randint(1, 10)

print("let's guess some numbers, shall we?\n")
print('number has been selected, go with your guesses:\n')

while points > -1:
    guess = int(input())

    if guess < value:
        print("The actual value is greater than your guess\n")
        points = points - 1

    if guess > value:
        print("The actual value is less than your guess\n")
        points = points - 1

    if guess == value:
        print("\nGood job!")
        break

    if points <= 0:
        print("You're run out of points!")
        break

    continue

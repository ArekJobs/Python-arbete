# Arek's guessing game
import random

# Intro
print("Made by Arek")
print("\nHello, welcome to this guessing game!")
print("_______________________________________________________________________________________________________________")

# All Values
MAX_NUM = int(input("Enter a big number: "))
X = random.randrange(0, MAX_NUM)
GUESS = int(input("Enter a guess: "))
AMOUNT_OF_GUESSES = 0
TOTAL_SCORE = 0

# Game loop
while GUESS != X:
    if GUESS < X:
        print("Higher")
        GUESS = int(input("Guess again: "))
        AMOUNT_OF_GUESSES += 1

    elif GUESS > X:
        print("Lower")
        GUESS = int(input("Guess again: "))
        AMOUNT_OF_GUESSES += 1
        print("You did it in", AMOUNT_OF_GUESSES + 1, "tries!")
        break

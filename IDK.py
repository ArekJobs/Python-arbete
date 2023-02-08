
# Guessing game

# modules
import random
import time

# Intro
print("Made by Arek")
print("\nHello, welcome to this guessing game!")
print("_______________________________________________________________________________________________________________")

# All values
MAX_NUM = (int(input("Enter the limit: ")))
X = random.randrange(MAX_NUM)
attempts = 0
ALLOWED_ATTEMPTS = 0

# Allowed Attempts
if MAX_NUM <= 50:
    ALLOWED_ATTEMPTS += 5

elif MAX_NUM <= 100:
    ALLOWED_ATTEMPTS += 10

else:
    ALLOWED_ATTEMPTS += 15

# Game loop
print("Perfect, lets start. You get", ALLOWED_ATTEMPTS, "attempts!")
time.sleep(1.2)
while True:
    attempts += 1
    ALLOWED_ATTEMPTS -= 1
    guess = int(input("Guess a number: "))
    if guess < X:
        print("Higher")

    elif guess > X:
        print("lower")

    else:
        print("You guessed the right number in", attempts, "attempts!")
        break

    if ALLOWED_ATTEMPTS == 0:
        print("\nOops, it looks like you are out of attempts, pleas try again.")
        quit()

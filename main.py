
import random
import time


# Name and Age
print("You have to be 16 or older to play")
time.sleep(1)
name = input("Enter you name: ")
print(f"Hello {name}!")

time.sleep(1.2)
def get_age():
    while True:
        age = input("Enter you´re age: ")
        try:
            checker = int(age)
            if checker >= 16:
                print("Great, it looks like you are old enough!\n")
                break
            else:
                print("Sorry, it looks like you are to young")
        except ValueError:
            print("Amount must be a number, try again")
    return checker
get_age()

# Username and password
test_user = ''.join((random.choice('abcdefghijklmnopqrstuvw123456789') for i in range(7)))
test_pass = ''.join((random.choice('abcdefghijklmnopqrstuvw123456789') for n in range(7)))

time.sleep(1.2)
print(f"You're preset username is '{test_user}'")
time.sleep(1)
print(f"You're preset password is '{test_pass}'")
time.sleep(1)
print("You will be able to change this later")

time.sleep(1.5)
userName = input("\nNow enter you're username and password. \nUsername: ")
password = input("Password: ")

count = 0
count += 1

while userName == test_user and password == test_pass:

    if count == 3:
        print("\nThree attempts used. Goodbye")
        break

    elif userName == test_user and password == test_pass:
        print(f"Welcome {name}!")
        break

    elif userName != test_user and password != test_pass:
        print("Your Username and Password is wrong!")
        userName = input("\n\nUsername: ")
        password = input("Password: ")
        count += 1
        continue

    elif userName == test_user and password != test_pass:
        print("Your Password is wrong, try again")
        userName = input("\n\nUsername: ")
        password = input("Password: ")
        count += 1
        continue

    elif userName != test_user and password == test_pass:
        print("Your Username is wrong!")
        userName = input("\n\nUsername: ")
        password = input("Password: ")
        count += 1
        continue


# change username and password
Reset = input("\nDo you want to change you're username and password?: ")
if Reset.lower() == "yes":
    userName = input("Enter new username here: ")
    password = input("Enter new password here: ")


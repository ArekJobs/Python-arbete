
def new_password(user_password):
    print("You're password has to be 8 characters or longer")
    user_password = input("Enter you're new password: ")
    if len(user_password) >= 8:
        print("Perfect, it looks like you're code is lng enough")
    else:
        print("You're password has to be loger!")

    if 'ä' in user_password or 'ä' in user_password or 'ö' in user_password:
        print("Password can't contain å,ä,ö")

new_password(user_password='')


new_string = input("Enter something: ")
def count(strings):
    letter_count = digit_count = 0

    for c in new_string:
        if c.isdigit():
            digit_count += 1
        elif c.isalpha():
            digit_count += 1

    return letter_count, digit_count

letters, digits = count(strings='')

print("Number of letters: ", letters)
print("Number of digits: ", digits)
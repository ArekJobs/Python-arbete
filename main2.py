
user_input = input("Enter a string: ")
counted = {"Numbers":0,"Letters":0}

for i in user_input:
    if i.isalpha():
        counted["Letters"] += 1
    elif i.isdigit():
        counted["Numbers"] += 1

print(counted)

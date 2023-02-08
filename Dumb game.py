ans = "yes"
while ans.lower() == "yes":
    ans = input("Do you want to play?: ")
print("I didn't even want to play")

i = 0
while i <= 20:
    i += 1
    if i % 2 == 0:
        print(i)

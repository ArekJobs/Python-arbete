#uppgift 1
A = input("Type a sentence: ")
for letter in A:
    print("(" + letter + ")")

#uppgift 2
B = int(input("n= "))
for i in range(B):
    print("|" + (" " * i) + "\ ")

#uppgift 3
n = int(input("Skriv ett nummer: "))
for index in range(n+1):
 if index == 1:
    print(" " + "_" * n)
 if index << n:
    print("|" + " " * n + "|")
 if index >= n:
    print(" " + "-" * n)

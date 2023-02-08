#Numbers and operators
op = input("Enter a operator: ")
num1 = float(input("Enter a number: "))
num2 = float(input("Enter a number: "))

#Main cakculator
if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
elif op == "**":
    print(num1 ** num2)
elif op == "//":
    print(num1 // num2)
elif op == "%":
    print(num1 % num2)
else:
    print("Sorry, invalid operator")

num1 = int(input("chose a number: "))
num2 = int(input("chose another number: "))
num3 = int(input("chose a last number: "))
if num1 <= num2 and num1 <= num3:
    print(str(num1) + " Is the smallest")
elif num2 <= num1 and num2 <= num3:
    print(str(num2) + " Is the smallest")
else:
    print(str(num3) + " is the smallest")

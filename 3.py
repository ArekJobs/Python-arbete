# Random
#Uppgift 1
import random
from random import sample
mylist = []

for i in range(30,50):
   x = random.randrange(10)
   mylist.append(x)
print(sample(mylist,10))

#Uppgift 2
list2 = []

for i in range(1, 11):
   a = (round(random.uniform(1, 10), 2))
   list2.append(a)
print(list2)

#Uppgift 3
import random
list = []
a = 50
b = 25

for i in range(7):
   c = random.gauss(a, b)
   list.append(c)
print(list)

#Uppgift 4
import random
list1 = ["hej", "shante", "Abdi", "les gooo", "Da baby"]
A = 2
print(random.sample(list1,A))

# Break
n = 0
while n < 100:
   n += 1
   if n == 51:
       break
   print(n)

# Try/except
a = input("Choose word:")
b = input("Choose number: ")
try:
   print(a + b)
except ValueError:
   print("Catch Error")

# Hantering av error vid division med 0
x = 1
y = 0
try:
   a = x / y
except ZeroDivisionError:
   a = 0

# Vecka 38, Uppgift 2
sen = input(str("Välj en mening: "))

A = (sen.count(" ")+1)
print(A)

x = sen.rindex("a")
print(x)

y = sen.endswith(".")
print(y)

B = sen.title()
C = B.swapcase()
print(C)

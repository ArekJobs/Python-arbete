# Uppgift 1,1
list1 = ["Arek", "Bill", "Rasmus", "Axel", "Szymon"]
# Uppgift 1,2
list2 = list1.copy()
print(list2)
# Uppgift 1,3
list2.reverse()
print(list2)
# Uppgift 1,4
element1 = (list2[0])
# Uppgift 1,5
list1.insert(2, element1)
print(list1)
# Uppgift 1,6
Antal_Szymon = list1.count(element1)
print(Antal_Szymon)

# Uppgift 2,1
lista1 = [65, 86, 53, 12, 16,]
# Uppgift 2,2
lista2 = [60, 70, 80, 90, 10]
lista1.append(87)
print(lista1)
lista1.extend(lista2)
print(lista1)
lista1.pop()
print(lista1)
lista1.remove(12)
print(lista1)

lista3 = [20, 89, 64, 0, 97]
def get_elements(list):
    count = 0
    for element in list:
        count += 1
    return count
print(get_elements(lista3))


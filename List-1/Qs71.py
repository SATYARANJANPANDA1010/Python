# Shallow Copy
list1 = [10, 20, 30, 40, 50]
list2 = list1.copy()
print(list1, list2)

l1 = [[10, 20], 30, 40]
l2 = l1.copy()
print(l1, l2)
l1[0].append(50)
print(l1)
print(l2)
l2[0][0] = 99
print(l1)
print(l2)

del l1[0][1]
print(l1)
print(l2)
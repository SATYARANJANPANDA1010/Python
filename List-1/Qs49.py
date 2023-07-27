# 2. Using del keyword
# delete more than one element using Slicing

list1 = list("PROGRAMMING")
print(list1)

del list1[:3]
print(list1)

del list1[-3:]
print(list1)

del list1[1:-1]
print(list1)

list2 = list(range(10, 110, 10))
print(list2)

del list2[:]    # delete all the elements in the list
print(list2)

list3 = list(range(10, 110, 10))
print(list3)

del list3[::-1]
print(list3)

list4 = list(range(10, 110, 10))
print(list4)

del list4[-1:-5:-1]
print(list4)
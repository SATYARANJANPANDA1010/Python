# Interchange first and last elements in a list

list1 = [10, 20, 30, 40, 50, 60, 70]
list1[0], list1[-1] = list1[-1], list1[0]
list1[2], list1[-2] = list1[-2], list1[2]
print(list1)
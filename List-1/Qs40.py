# GFG - List
# Python program to interchange first and last elements in a list
# Input : [12, 35, 9, 56, 24]
# Output : [24, 35, 9, 56, 12]
# Input : [1, 2, 3]
# Output : [3, 2, 1]

list1 = [12, 35, 9, 56, 24]
list1[0], list1[-1] = list1[-1], list1[0]
print(list1)

list2 = [1,2,3]
list2[0],list2[-1] = list2[-1],list2[0]
print(list2)
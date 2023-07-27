# GFG
# Python program to print odd numbers in a List
# Input: list1 = [2, 7, 5, 64, 14] 
# Output: [7, 5]
# Input: list2 = [12, 14, 95, 3, 73]
# Output: [95, 3, 73]

list1 = [2, 7, 5, 64, 14]
odd_list1 = []
for i in list1:
    if i % 2 != 0:
        odd_list1.append(i)
print(odd_list1)

list2 = [12, 14, 95, 3, 73]
odd_list2 = []
for i in list2:
    if i % 2 != 0:
        odd_list2.append(i)
print(odd_list2)

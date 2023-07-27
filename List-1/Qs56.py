# GFG
# Python program to print negative numbers in a list
# Input: list1 = [12, -7, 5, 64, -14]
# Output: -7, -14

# Input: list2 = [12, 14, -95, 3]
# Output: -95

list1 = [12, -7, 5, 64, -14]
for ele in list1:
    if ele < 0:
        print(ele, end=" ")

print()
list2 = [12, 14, -95, 3]
for ele in list2:
    if ele < 0:
        print(ele, end=" ")




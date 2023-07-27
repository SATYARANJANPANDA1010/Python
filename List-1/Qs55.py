# Python program to print positive numbers in a list
# Input: list1 = [12, -7, 5, 64, -14]
# Output: 12, 5, 64

# Input: list2 = [12, 14, -95, 3]
# Output: [12, 14, 3]

list1 = [12, -7, 5, 64, -14]
for i in list1:
    if i >= 0:
        print(i, end=" ")

print() # for new line

list2 = [12, 14, -95, 3]
for ele in list2:
    if ele >= 0:
        print(ele, end=" ")

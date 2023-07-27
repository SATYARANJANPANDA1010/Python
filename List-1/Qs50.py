# GFG
# Python program to print even numbers in a list

# Input: list1 = [2, 7, 5, 64, 14]
# Output: [2, 64, 14]
# Input: list2 = [12, 14, 95, 3]
# Output: [12, 14]

list1 = [2, 7, 5, 64, 14]
even_list = []
for i in list1:
    if i % 2 == 0:
        even_list.append(i)
print(even_list)

list2 = [12, 14, 95, 3]
even_list1 = []
for i in list2:
    if i % 2 == 0:
        even_list1.append(i)
print(even_list1)





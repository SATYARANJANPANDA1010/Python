# GFG - List
# Python program to swap two elements in a list
# Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
# Output : [19, 65, 23, 90]
# Input : List = [1, 2, 3, 4, 5], pos1 = 2, pos2 = 5
# Output : [1, 5, 3, 4, 2]

list1 = [23, 65, 19, 90]
print(f'before swaping {list1}')
pos1 = int(input("Enter pos1: "))
pos2 = int(input("Enter pos2: "))
list1[pos1-1], list1[pos2-1] = list1[pos2-1], list1[pos1-1]
print(f'after swaping {list1}')
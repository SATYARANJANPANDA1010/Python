# Difference between two lists
'''
Input:
list1 = [10, 15, 20, 25, 30, 35, 40]
list2 = [25, 40, 35]

Output:
[10, 20, 30, 15]

Explanation:
resultant list = list1 - list2
'''
list1 = [10, 15, 20, 25, 30, 35, 40]
list2 = [25, 40, 35]
set1 = set(list1)
set2 = set(list2)
# Method-1
list3 = sorted(set1-set2)
print(list3)
# Method-2
set3 = set1-set2
list4 = list(set3)
print(list4)


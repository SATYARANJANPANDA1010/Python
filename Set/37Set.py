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
list3 = []
for value in list1:
    if value not in list2:
        list3.append(value)
print(f'Difference between list1 and list2 {list3}')

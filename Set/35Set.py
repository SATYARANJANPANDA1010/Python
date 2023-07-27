# Find missing and additional values in two lists
'''
Input : list1 = [1, 2, 3, 4, 5, 6]
        list2 = [4, 5, 6, 7, 8]
Output : Missing values in list1 = [8, 7]
         Additional values in list1 = [1, 2, 3]
         Missing values in list2 = [1, 2, 3]
         Additional values in list2 = [7, 8]

'''
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8]
set1 = set(list1)
set2 = set(list2)
print(f'Missing values in list1 = {sorted(set2-set1)}')
print(f'Additional values in list1 =  {sorted(set1-set2)}')
print(f'Missing values in list2 = {sorted(set1-set2)}')
print(f'Missing values in list2 = {sorted(set2-set1)}')

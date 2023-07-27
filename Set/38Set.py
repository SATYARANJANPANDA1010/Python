# Python Set difference to find lost element from a duplicated array
'''
Input:  A = [1, 4, 5, 7, 9]
        B = [4, 5, 7, 9]
Output: [1]
1 is missing from second array.

Input: A = [2, 3, 4, 5
       B = 2, 3, 4, 5, 6]
Output: [6]
6 is missing from first array.
'''
A = [1, 4, 5, 7, 9]
B = [4, 5, 7, 9]
set1 = set(A)
set2 = set(B)
if len(set1) > len(set2):
    print(f'{list(set1-set2)} is missing from second array')
else:
    print(f'{list(set2-set1)} is missing from first array')
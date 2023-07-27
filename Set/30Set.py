# GFG | Python program to find common elements in three lists using sets
'''
Input : ar1 = [1, 5, 10, 20, 40, 80]
        ar2 = [6, 7, 20, 80, 100]
        ar3 = [3, 4, 15, 20, 30, 70, 80, 120]

Output : [80, 20]

Input : ar1 = [1, 5, 5]
        ar2 = [3, 4, 5, 5, 10]
        ar3 = [5, 5, 10, 20]

Output : [5]
'''
# Method - 1
ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]
set1 = set(ar1)
set2 = set(ar2)
set3 = set(ar3)
set4 = set1 & set2 & set3
print(list(set4))

# Method-2
ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]
set_common = set()
set_a = set(ar1)
set_b = set(ar2)
set_c = set(ar3)

for value in set_a:
    if value in set_b and value in set_c:
        set_common.add(value)
print(list(set_common))


# Method - 3 (List)
ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]

common_ele = []
for value in ar1:
    if value in ar2 and value in ar3:
        common_ele.append(value)
print(common_ele)

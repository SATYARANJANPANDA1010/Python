# GFG | Check if two lists have at-least one element common
'''
Input : a = [1, 2, 3, 4, 5]
        b = [5, 6, 7, 8, 9]
Output : True

Input : a=[1, 2, 3, 4, 5]
        b=[6, 7, 8, 9]
Output : False
'''

a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]
set1 = set(a)
set2 = set(b)
if set1 & set2:
    print("True")
else:
    print("False")

# Another Method
a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]
set_a = set(a)
set_b = set(b)
if len(set_a.intersection(set_b))>0:
    print("True")
else:
    print("False")



# Another Method
a=[1, 2, 3, 4, 5]
b=[6, 7, 8, 9]
set_A = set(a)
set_B = set(b)
result = False
for x in set_A:
    for y in set_B:
        if x == y:
            result = True
print(result)


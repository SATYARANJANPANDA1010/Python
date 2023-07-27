# deep copy
# deep copy is a object copy
# deep copy creates independent copy of the original object.
# In deep copy, Python Virtual Machine Create a new list by storing copy of the objects exist within old list
# after creating new list , if changes have been made it will not reflect to old list.
import copy
l1 = [10, [30, 40]]
l2 = copy.deepcopy(l1)
print(l1)
print(l2)
l1[1][0] = 20
print(l1)
print(l2)
del l2[1][0]
print(l1)
print(l2)
# Shallow Copy
# using "copy" module
import copy
l1 = [10, [20, 30]]
l2 = copy.copy(l1)
print(l1)
print(l2)
l1[1][0] = 40
print(l1)
print(l2)

del l1[0]
print(l1)
print(l2)
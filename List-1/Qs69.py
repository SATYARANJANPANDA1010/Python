# + operator adding sequences. So, list is sequence type.
# extend() method adds the specified list elements (or any iterables) to the end of the element of the current list.

l1 = [10, 20, 30] + [40, 50, 60]
print(l1)

l2 = [1, 2, 3, 4]
l2 += [5, 6, 7, 8, 9, 10]
print(l2)

l3 = [10, 20, 30, 40]
l3.extend([50, 60, 70, 80])
print(l3)

# Another Example

lst1 = [1, 2, 3, 4, 5, 6]
lst2 = [7, 8, 9, 10]
lst1.extend(lst2)
print(lst1)
print(lst2)
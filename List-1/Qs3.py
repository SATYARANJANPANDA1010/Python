# Creating list with list() or list(iterables)
# This syntax allows to create list using existing iterables or collections
# converting other iterables/collections into list type

# Creating empty list using list()
list1 = list()
print(list1)

list2 = list("SATYA")
print(list2)

list3 = [10, 20, 30, 40, 50]
list4 = list(list3)
list5 = list3


print(list3)
print(id(list3)) # prints the ID of list3 object

print(list4)
print(id(list4))  # prints the ID of list4 object

print(list5)
print(id(list5))  # prints the ID of list5 object
# Operators used with list
# + -->  used for concatenation of list
# * -->  used to repeat sequence
# == --> used to compare the element in the list

# + -->  used for concatenation of list
list1 = [10, 20, 30, 40, 50, 60]
list2 = [40, 50, 60, 70, 80, 90]
list3 = list1+list2
print(list1, list2, list3, sep="\n")

# * -->  used to repeat sequence
list4 = list1 * 2
print(list4)

# == --> used to compare the element in the list
print(list1 == list2)

list6 = list1.copy()
print(list6)
print(list1 == list6)





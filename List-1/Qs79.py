# sort()

list1 = [10, 5, 8, 2, 4, 5, 1, 9, 20, 12, 10, 23, 56, 2, 7, 8, 9]
list2 = list1.sort()
print(list1)

list3 = ["a", "b", "A", "B", "c", "d", "D", "C"]

list4 = list3.sort()
print(list3)

list5 = list3.sort(key = str.upper)
print(list3)

list6 = list3.sort(key = str.lower)
print(list3)

list7 = list3.sort(key = str.lower,reverse=True)
print(list3)
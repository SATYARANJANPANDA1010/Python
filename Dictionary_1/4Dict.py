dict1 = dict()
print(dict1)  # empty dictionary

# if you want to convert list into dictionary , then list should contain tuple.
# Because dictionary should contain keys and values.
list1 = [(1, 10), (2, 20), (3, 30), (4, 40), (5, 50)]
dict2 = dict(list1)
print(dict2)

list2 = [10, 20, 30, 40, 50]
e = enumerate(list2,1)
dict3 = dict(e)
print(dict3)

list3 = list(range(1,11))
en = enumerate(list3,100)
print(dict(en))
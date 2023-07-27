# I have a two list

list1 = [1,2,3,4,5]
list2 = [10,20,30,40,50]
list3 = [(list1[i],list2[i]) for i in range(5)]
print(list3)

dict1 = dict(list3)
print(dict1)
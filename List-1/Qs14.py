# syntax : sequence-name[start:stop]
list1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
list2 = list1[2:5]
print(list2)
list3 = list1[-5:-2]
print(list3)

# if start-index > stop-index, so it will return empty list
list4 = list1[5:2]
print(list4)
list5 = list1[-1:-5]
print(list5)

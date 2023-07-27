# syntax : sequence-name[::step]
# if step value is +ve . Start-index = 0 and stop-index is taken based on step value
# if step value is -ve . Start index = -1 and stop-index  = -(len of sequence+1)

list1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
list2 = list1[::1]
print(list2)
list3 = list1[::2]
print(list3)
list4 = list1[::-1]
print(list4)
list5 = list1[::-2]
print(list5)

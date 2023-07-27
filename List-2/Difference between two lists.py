list1=[10,15,20,25,30,35, 40]
list2=[25,40,35]
#first method
A = set(list1)
B = set(list2)
C = list(A-B)
print(f'Difference between two list {C}')

#second method
list3 = []
for values in list1:
    if values not in list2:
        list3.append(values)
print(f'Difference between two list {list3}')

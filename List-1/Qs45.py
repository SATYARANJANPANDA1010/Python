# GFG
# Find sum of elements in list

n = int(input("Enter how many elements: "))
list1 = []
for i in range(n):
    ele = int(input("Enter elements: "))
    list1.append(ele)
print(list1)
add = 0
for i in list1:
    add = add+i
print(f'Sum of the element is : {add}')

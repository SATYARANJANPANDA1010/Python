n = int(input("howmany elements in the list: "))
list1 = []
for i in range(n):
    ele = int(input("Enter the elements"))
    list1.append(ele)
print(list1)
sum = 0
for i in list1:
    sum = sum+i
print(f"sum of the elements is: {sum}")

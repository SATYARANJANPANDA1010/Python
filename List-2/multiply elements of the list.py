n = int(input("howmany elements in the list: "))
list1 = []
for i in range(n):
    ele = int(input("Enter the elements"))
    list1.append(ele)
print(list1)
mul = 1
for i in list1:
    mul = mul*i
print(f"multiply of the elements is: {mul}")

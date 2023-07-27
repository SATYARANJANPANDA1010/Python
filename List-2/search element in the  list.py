n = int(input("Enter howmany elements: "))
list1 = []
for i in range(n):
    value = int(input("Enter the values"))
    list1.append(value)
s = int(input("Enter the value to search"))
print("exist") if s in list1 else print("not exist")


# GFG
# Check if element exists in list in Python

n = int(input("Enter howmany elements: "))
list1 = []
for i in range(n):
    value = int(input("Enter any values: "))
    list1.append(value)

s = int(input("Enter value to search: "))
print("exists") if s in list1 else print("not exists")



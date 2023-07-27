def linear_search(list,element):
    for i in range(len(list)):
        if list[i] == element:
            return i


n = int(input("Enter Howmany Input Element:  "))
li = []
for num in range(n):
    value = int(input("enter the element"))
    li.append(value)
ele = int(input("Element you want to search: "))
index = linear_search(li,ele)
print(index)

str1 = "NARESH"
str2 = sorted(str1)
print(str1)
print(str2)

str3 = sorted(str1,reverse=True)  # reverse = True , it means arrange descending to ascending
print(str3)

# syntax --> sorted(iterables,key,reverse=False)
list1 = [4, 8, 9, 2, 1, 7, 5, 3]
list2 = sorted(list1)
list3 = sorted(list1,reverse=True)
print(list1)
print(list2)
print(list3)
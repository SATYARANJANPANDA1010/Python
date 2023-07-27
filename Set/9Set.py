# str1 = "abcabcc"
# output: 2a2b3c
# sorted format
str1 = "abcabcc"
list1 = sorted(set(str1))
print(list1)
str2 = ""
for value in list1:
    c = str1.count(value)
    str2 = str2+str(c)+value
print(str2)


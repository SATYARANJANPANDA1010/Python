# str1 = "abcabcc"
# output: 2a2b3c

str1 = "abcabcc"
set1 = set(str1)
str2=""
for value in set1:
    c = str1.count(value)
    str2 = str2+str(c)+value
print(str1)
print(str2)
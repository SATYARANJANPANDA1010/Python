str1 = input("Enter a string: ")
set1 = set(str1)  # remove the duplicate elements
str2 = ""  # empty string

for value in set1:
    c = str1.count(value)
    str2 = str2+str(c)+value
print(str1)
print(str2)


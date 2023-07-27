# Example:3
# create dictionary with name as a key
# and 2 subject marks as value
# read the details of n students
n = int(input("Enter Howmany Students: "))
dict3 = {}
for i in range(n):
    name = input("Enter the name")
    marks = [int(input("Enter Marks:" )) for j in range(2)] #list comprehension
    dict3[name] = marks
print(dict3)


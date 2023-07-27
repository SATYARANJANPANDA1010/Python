# create ASCII chart dictionary
dict1 = {}
for i in range(65,91):
    dict1[chr(i)] = i
print(dict1)
# Using comprehension
dict2 = {chr(num):num for num in range(65,91)}
print(dict2)
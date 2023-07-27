# Dictionary Comprehension
dict1 = {}
n = int(input("Enter a number: "))
for num in range(1,n+1):
    dict1[num] = num**2
print(dict1)
# comprehension
dict2 = {num:num**2 for num in range(1,n+1)}
print(dict2)

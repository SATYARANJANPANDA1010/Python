# Comprehension
# create a list with sqr of all the numbers from 1 to 50

# with out using Comprehension
list1 = []
for num in range(1,51):
    list1.append(num**2)
print(list1)

# Using Comprehension
list2 = [num**2 for num in range(1,51)]
print(list2)
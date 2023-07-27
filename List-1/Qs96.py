# Syntax 2: Creating List based on test condition or Boolean expression
# list_name = [expression/value for variable in iterable if test/condition]
# without Comprehension
list1 = []
for i in range(1,51):
    if i % 5 == 0:
        list1.append(i)
print(list1)

# Using comprehension
list2 = [i for i in range(1,51) if i % 5 == 0]
print(list2)



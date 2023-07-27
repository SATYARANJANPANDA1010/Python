# GFG
# Python program to find the sum of all items in a dictionary
# Input : {‘a’: 100, ‘b’:200, ‘c’:300}
# Output : 600
#
# Input : {‘x’: 25, ‘y’:18, ‘z’:45}
# Output : 88
dict1 = {'a': 100, 'b': 200, 'c': 300}
sum = 0
for i in dict1.values():
    sum = sum+i
print(f'Sum of values: {sum}')


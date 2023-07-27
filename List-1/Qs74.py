# GFG
# Python | Count occurrences of an element in a list
# Input: lst = [15, 6, 7, 10, 12, 20, 10, 28, 10], x = 10
# Output: 3
# Explanation: 10 appears three times in given list.

lst = [15, 6, 7, 10, 12, 20, 10, 28, 10]
count = 0
x = int(input("Enter the number: "))

while x in lst:
    lst.remove(x)
    count = count+1
print(f'{x} appears {count} times in given list')



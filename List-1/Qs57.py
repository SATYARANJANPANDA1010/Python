# GFG
# Python program to print all positive numbers in a range
# Input: start = -4, end = 5
# Output: 0, 1, 2, 3, 4, 5

# Input: start = -3, end = 4
# Output: 0, 1, 2, 3, 4

start = int(input("Enter start range: "))
end = int(input("Enter end range: "))
for i in range(start, end+1):
    if i >= 0:
        print(i, end=" ")



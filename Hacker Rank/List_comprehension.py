# https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true

# without using Comprehension
x = 1
y = 1
z = 1
n = 2
list1 = []
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if i+j+k != n:
                list1.append([i, j, k])
print(list1)

# Using Comprehension
list2 = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != 1]
print(list2)

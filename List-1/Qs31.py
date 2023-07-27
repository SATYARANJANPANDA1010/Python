# write a program to generate sqr's all numbers from 1 to n
# sum of all squares
n = int(input("Enter n value"))
r = range(1, n+1)
s = 0
for i in r:
    print(f'{i} --> {i**2}')
    s = s+(i**2)
print(f'Sum of square is {s}')


# Another one
num = int(input("Enter a numbers: "))
sum = 0
for i in range(1, num + 1):
    print(f'{i}--->{i * i}')
    sum = sum+(i*i)

print(f'Sum of the squares is {sum}')

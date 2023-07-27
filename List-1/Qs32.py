# WAP to print sum of n numbers
# input n numbers from keyboard

n = int(input("Number of input: "))
s = 0
for i in range(n):
    num = int(input("Enter a number: "))
    s = s+num
print(f'Sum of n numbers is {s}')
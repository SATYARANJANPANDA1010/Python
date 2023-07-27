# WAP to generates prime numbers
# between m to n
m = int(input("Enter value of m: "))
n = int(input("Enter value of n: "))
for num in range(m,n+1):
    c = 0
    for i in range(1,num+1):
        if num%i == 0:
            c = c+1
    if c == 2:
        print(num)
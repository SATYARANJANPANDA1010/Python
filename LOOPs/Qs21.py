# WAP to generate factorials of all numbers between m to n
m = int(input("Enter m value: "))
n = int(input("Enter n value: "))
for i in range(m,n+1):
    fact = 1
    for j in range(1,i+1):
        fact = fact * j
    print(f'{i} --> {fact}')

# write a program to find input number is prime or not

num = int(input("Enter any number: "))
i = 1
c = 0
while i<=num:
    if num%i==0:
        c=c+1
    i=i+1
if c ==2:
    print(f'{num} is a prime number')
else:
    print(f'{num} is not a prime number')
    

#WAP to find sum of digits of input number
#125 --> 1+2+5 = 8

num = int(input("Enter any number"))
sum = 0
while num>0:
    rem = num%10
    sum = sum+rem
    num = num//10
print(f'sum of digits is {sum}')

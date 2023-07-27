# write a program to find reverse of a number
num = int(input("Enter a number: "))
rev = 0
num1 = num
while num>0:
    rem = num%10
    rev = (rev*10)+rem
    num = num//10
print(f'{num1} of reverse is {rev}')

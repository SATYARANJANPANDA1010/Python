# write a program is a Palindrome number

num = int(input("Enter a number: "))
rev = 0
num1 = num
while num>0:
    rem = num%10
    rev = (rev*10)+rem
    num = num//10
if rev == num1:
    print(f'{num1} is a palindrome number')
else:
    print(f'{num1} is not a palindrome number')

#write a program to find input number is armstrong number or not

num = int(input("Enter any number"))
num1 = num
length = len(str(num))
s = 0
while num>0:
    rem = num%10 #for each digit
    s = s+(rem**length) 
    num=num//10
if s == num1:
    print(f'{num1} is armstrong number')
else:
    print(f'{num1} is not armstrong number')
    

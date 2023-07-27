#Python Program to add two hexadecimal numbers\

num1 = int(input("Enter a number: "),base=16)
num2 = int(input("Enter a number: "),base=16)
sum = hex(num1+num2)
print(sum)
print(sum[2:])
#Python program to add two Octal numbers

num1 = int(input("Enter a number: "),base=8)
num2 = int(input("Enter a number: "),base=8)
sum = oct(num1+num2)
print(sum)
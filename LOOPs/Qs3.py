# WAP to print a math table of input number:
num = int(input("Enter any number: "))
i = 1
while i<=10:
    p = num * i
    print(f'{num}*{i}={p}')
    i = i+1
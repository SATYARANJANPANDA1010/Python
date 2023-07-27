#WAP to display sum of odd numbers and even numbers that fall between two numbers.

first = int(input("Enter a number: "))
second = int(input("Enter a number: "))
SumEven = 0
SumOdd = 0
for i in range(first,second+1):
    if i%2==0:
        SumEven = SumEven+i
    else:
        SumOdd = SumOdd+i
print(f'sum of even number is {SumEven}')
print(f'sum of odd number is {SumOdd}')
        

# Factorial Number using while loop
num = int(input("Enter a number: "))
fact = 1
starts = 1
while starts<=num:
    fact = fact*starts
    starts = starts+1
print(f'Factorial of {num} is {fact}')
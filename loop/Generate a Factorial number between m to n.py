#WAP generate Factorial Number between m to n

m = int(input("Enter the staring number: "))
n = int(input("Enter the ending number: "))
for num in range(m,n+1):
    fact = 1
    for i in range(1,num+1):
        fact = fact*i
    print(f'{num} of Factorial is -->{fact}')
        

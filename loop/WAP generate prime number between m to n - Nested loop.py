#WAP generate prime number between m to n

m = int(input("Enter the starting number: "))
n = int(input("Enter the ending number: "))
for num in range(m,n+1):
    count = 0
    for i in range(1,num+1):
        if num%i == 0:
            count = count+1
    if count == 2:
        print(num)
        
        
            

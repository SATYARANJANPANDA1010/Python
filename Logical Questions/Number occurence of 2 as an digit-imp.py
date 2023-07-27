#Number of occurence of 2 as a digit in numbers from 1 to n

num = int(input("Enter num: "))
lis = []
c=0
for i in range(1,num+1):
    lis.append(i)

for num1 in lis:
    while num1>0:
        rem = num1%10
        if rem==2:
            c=c+1
        num1 = num1//10
print(c)
          
        
        

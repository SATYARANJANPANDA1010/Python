n = int(input("Enter value of n"))
lis=[]
for i in range(n):
    num = int(input("Enter the value: "))
    lis.append(num)
print(lis)
#add list values
s = 0
for num in lis:
    s = s+num
print(f"sum of the list values: {s}")
    

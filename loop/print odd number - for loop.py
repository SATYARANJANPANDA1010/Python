#print odd number - 1 to 30

for num in range(1,30):
    if num%2!=0:
        print(num)

#Another method
for num in range(1,31,2):
    print(num,end=" ")

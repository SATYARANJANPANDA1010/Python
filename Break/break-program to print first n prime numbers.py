#program to print first n prime numbers

n = int(input("Howmany prime numbers: "))
num=2
pcount=0 #prime number count
while True:
    c=0
    for i in range(1,num+1):
        if num%i==0:
            c=c+1
    if c==2:
        print(num)
        pcount=pcount+1
    if pcount>=n:
        break
    num=num+1

n = int(input("Enter a number: "))
for r in range(1,n+1):
    for c in range(n,0,-1):
        if r==c:
            print("*",end=" ")
        else:
            print(c,end=" ")
    print()
n = int(input("Enter a number: "))
for r in range(1,n+1):
    for c in range(1,r+1):
        if c>1 and r>c:
            print("2",end=" ")
        else:
            print("1",end=" ")
    print()
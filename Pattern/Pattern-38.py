for r in range(1,5):
    for c in range(1,r+1):
        if c>1 and r>c:
            print("0",end=" ")
        else:
            if r>1:
                print(r-1,end=" ")
            else:
                print(r,end=" ")
    print()

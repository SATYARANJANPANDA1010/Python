for r in range(1,6):
    for c in range(1,r+1):
        if r%2 ==0:
            if c%2 == 0:
                print("1",end=" ")
            else:
                print("0",end=" ")
        else:
            if c%2 == 0:
                print("0",end=" ")
            else:
                print("1",end=" ")
    print()
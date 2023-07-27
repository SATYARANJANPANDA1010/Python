'''
        1
      2 1
    3 2 1
  4 3 2 1
5 4 3 2 1
'''
for i in range(1,6):
    for j in range(5,0,-1):
        if j<=i:
            print(j,end=" ")
        else:
            print(" ",end=" ")
    print()
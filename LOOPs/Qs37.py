'''
        5
      4 5
    3 4 5
  2 3 4 5
1 2 3 4 5
'''
for i in range(5,0,-1):
    for j in range(1,6):
        if j>=i:
            print(i,end=" ")
        else:
            print(" ",end=" ")
    print()


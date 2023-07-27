#Pattern-16

'''
        1 
      1 2 
    1 2 3 
  1 2 3 4 
1 2 3 4 5 
'''
for r in range(1,6):
    num = 1
    for c in range(5,0,-1):
        if c>r:
            print(" ",end=" ")
        else:
            print(num,end=" ")
            num=num+1
    print()

'''
1 2 3 4 5 6 
  2 3 4 5 6 
    3 4 5 6 
      4 5 6 
        5 6 
          6 
          6 
        5 6 
      4 5 6 
    3 4 5 6 
  2 3 4 5 6 
1 2 3 4 5 6
'''
spaces = 0
num=1
for r in range(1,7):
    for s in range(spaces):
        print(" ",end=" ")
    for c in range(1,7):
        if c>=r:
            print(c,end=" ")
            num=num+1
    print()
    spaces=spaces+1
for r in range(6,0,-1):
    for c in range(1,7):
        if c>=r:
            print(c,end=" ")
        else:
            print(" ",end=" ")
    print()

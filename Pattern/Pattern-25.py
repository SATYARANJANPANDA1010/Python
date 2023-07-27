#Pattern-25

'''
1       1 
  2   2   
    3     
  4   4   
5       5 
'''

for r in range(1,6):
    for c in range(1,6):
        if r==c or r+c==6:
            print(r,end=" ")
        else:
            print(" ",end=" ")
    print()

#Pattern-26
'''
1       5 
  2   4   
    3     
  2   4   
1       5
'''

for r in range(1,6):
    for c in range(1,6):
        if r==c or r+c==6:
            print(c,end=" ")
        else:
            print(" ",end=" ")
    print()

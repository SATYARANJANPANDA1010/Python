#Pattern-24
'''
*       * 
  *   *   
    *     
  *   *   
*       * 
'''

for r in range(1,6):
    for c in range(1,6):
        if r==c or r+c==6:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

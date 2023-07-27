#Pattern-23
'''
*       * 
  *   *   
    *     
  *   *   
*       * 
'''
#1st Method

i = 0 #row initial value --> row value increases
j = 4 #column last value --> column value decreases
for row in range(5):
    for col in range(5):
        if row == i and col == j:
            print("*",end=" ")
            i = i+1
            j = j-1
        elif row==col:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
                










'''
n = 5
for r in range(n):
    for c in range(n):
        if ( r == c or r+c == n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
'''

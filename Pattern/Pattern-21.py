#Pattern-21

'''
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
* * * * * 
 * * * * 
  * * * 
   * * 
    * 
'''

spaces = 4
for r in range(1,6):
    for s in range(spaces):
        print(' ',end='')
    for c in range(1,r+1):
        print("*",end=' ')
    print()
    spaces=spaces-1
spaces=0
for r in range(5,0,-1):
    for s in range(spaces):
        print(' ',end='')
    for c in range(1,r+1):
        print("*",end=' ')
    
    print()
    spaces=spaces+1
    


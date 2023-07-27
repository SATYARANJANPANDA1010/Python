'''
            * 
          * * * 
        * * * * * 
      * * * * * * * 
    * * * * * * * * * 
  * * * * * * * * * * * 
* * * * * * * * * * * * * 
  * * * * * * * * * * * 
    * * * * * * * * * 
      * * * * * * * 
        * * * * * 
          * * * 
            *
'''

n = int(input("Enter odd number"))

for r in range(1,n+1):
    for space in range(1,n-r+1):
        print(" ",end=" ")
    for c in range(1,2*r):
        print("*",end=" ")
    print()
    
spaces=0
for r in range(n-1,0,-1):
    for space in range(spaces+1):
        print(" ",end=" ")
    for c in range(2*r-1):
        print("*",end=" ")
    print()
    spaces=spaces+1

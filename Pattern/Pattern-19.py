#Pattern-19
'''
* * * * * 
  * * * * 
    * * * 
      * * 
        * 
'''

for r in range(1,6):
    for c in range(1,6):
        if r<=c:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

'''
Enter odd number5
          * 
        * * * 
      * * * * * 
    * * * * * * * 
  * * * * * * * * * 
'''
n = int(input("Enter odd number"))
spaces = n

for r in range(n):
    for space in range(spaces):
        print(" ",end=" ")
    stars = 2*r+1
    for c in range(stars):
        print("*",end=" ")
    print()
    spaces=spaces-1

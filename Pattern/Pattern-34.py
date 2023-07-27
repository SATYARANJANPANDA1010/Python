'''
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
'''

n = int(input("Enter a number: "))
for r in range(1,n+1):
    for c in range(n,0,-1):
        print(c,end=" ")
    print()
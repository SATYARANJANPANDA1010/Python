'''
1
2 3
3 4 5
4 5 6 7
5 6 7 8 9
'''
n = int(input("Enter a number: "))
for r in range(1,n+1):
    for c in range(0,r):
        print(r+c,end=" ")
    print()

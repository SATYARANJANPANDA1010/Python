'''
1 2 3 4 5
2 3 4 5 6
3 4 5 6 7
4 5 6 7 8
5 6 7 8 9
'''

n = int(input("Enter a number: "))
for r in range(1,n+1):
    for c in range(n):
        print(r+c,end=" ")
    print()
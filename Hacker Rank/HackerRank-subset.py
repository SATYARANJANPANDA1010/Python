T = int(input())
for i in range(T):
    A = int(input())
    A1 = set(map(int,input().split()))
    B = int(input())
    B1 = set(map(int,input().split()))
    print(A1.issubset(B1))


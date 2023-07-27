# CODECHEF -- > https://www.codechef.com/problems/CANDYSTORE?tab=statement
# cook your dish here
T = int(input())
for i in range(T):
    X,Y = map(int,input().split())
    if Y<=X:
        print(Y)
    else:
        extra_chocolate = Y-X
        sell = X + (2 * extra_chocolate)
        print(sell)
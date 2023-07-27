# CODECHEF --> https://www.codechef.com/problems/SNDMAX?tab=statement
# Second Max of Three Numbers
# input:
# 3 --> test cases
# 1 2 3
# 10 15 5
# 100 999 500
# output
# 2
# 10
# 500
# cook your dish here
N = int(input("Enter number of test cases: "))
for i in range(N):
    a,b,c = map(int, input("Enter Elements: ").split())
    if (a>b and a<c) or (a<b and a>c):
        print(a)
    elif (b>a and b<c) or (b<a and b>c):
        print(b)
    else:
        print(c)
# Another Approach
T = int(input('Enter Number Of Test Cases: '))
for i in range(T):
    a,b,c = map(int, input("Enter Elements: ").split())
    lis = list((a,b,c))
    sort_lis = sorted(lis)
    print(sort_lis[1])
# Project Euler 1 : https://www.hackerrank.com/contests/projecteuler/challenges/euler001/problem?isFullScreen=true
t = int(input("Enter the number of test cases:"))

for i in range(t):
    sum = 0
    n = int(input("Enter a Number: "))
    for i in range(1,n):
        if i % 3 == 0 or i%5 == 0:
            sum =sum+i
    print(sum)
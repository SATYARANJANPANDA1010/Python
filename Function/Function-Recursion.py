# Find n factorial through Recursion

def fact(n):
    if n == 0:
        return 1
    return n*fact(n-1)


n = int(input("enter a number: "))
print(fact(n))
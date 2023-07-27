def fact(n):
    factorial = 1
    for i in range(1,n+1):
        factorial = factorial*i
    return factorial

def main():
    a = int(input("Enter a number: "))
    d = fact(a)
    print(f"Factorial of {a} is {d}")
main()
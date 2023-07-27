#Python program to print all Prime numbers in an Interval
# input n from user
n = int(input("Enter a number: "))

# iterate through 2 to n and print all prime numbers
print("Prime numbers from 2 to", n, "are:")
for num in range(2, n + 1):
    for i in range(2, num):
        if (num % i) == 0:
            break
    else:
        print(num)
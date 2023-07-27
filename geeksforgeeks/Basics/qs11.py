#check number is prime or not

num = int(input("Enter a number: "))
flag = False
for i in range(2,num):
    if num%i==0:
        flag = False
if flag:
    print(f"{num} is not a prime number")
else:
    print(f"{num} is a prime number")
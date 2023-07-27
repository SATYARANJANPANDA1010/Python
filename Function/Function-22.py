def armstrong(n):
    sum = 0
    temp=n
    while temp > 0:
        digit = temp % 10
        sum = sum + (digit ** 3)
        temp = temp // 10
    if sum == temp:
        print("Armstrong number")
    else:
        print("Not Armstrong number")



num = int(input("Enter a number: "))
length = len(str(num))
armstrong(num,length)
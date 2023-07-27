#Python Program to check Armstrong Number

num = int(input("Enter a number: "))
length = len(str(num))
temp = num
sum = 0
while temp>0:
    rem = temp%10
    sum = sum + (rem**length)
    temp = temp//10
if num == sum:
    print(f"{num} is a armstrong number")
else:
    print(f"{num} is not a armstrong number")

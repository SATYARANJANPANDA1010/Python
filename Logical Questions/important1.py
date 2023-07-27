# Input --> 983 --> sum each digit 9+8+3 = 17 ---> sum each digit of number 17 --> 1+7 -->Output --> 8
n = int(input("Enter a number: "))
count = 0
while n>0:
    rem = n%10
    count=count+rem
    n=n//10
    temp = count
    count1 = 0
    while temp>0:
        rem = temp%10
        count1 = count1+rem
        temp=temp//10
print(count1)

































'''
n = int(input("Enter the number: "))
li = []
c=0
for i in range(1,n+1):
    li.append(i)
# print(li)

for num in li:
    while num>0:
        rem = num%10
        if rem == 2:
            c=c+1
        num=num//10
print(c)
'''
num = int(input("Enter a number: "))
temp = num
product = 1
while temp>0:
    rem = temp%10
    product = product*rem
    temp = temp//10
print(f'{num} of product is {product} ')

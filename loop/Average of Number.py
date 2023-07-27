# write a program accept 10 number from user and display avg

total = 0
for i in range(10):
    num = int(input("Enter a number: "))
    total = total+num
avg = total/10

print(f'Average of number is {avg:.2f}')

# WAP accept 10 numbers from users and display avg
total = 0
for i in range(10):
    num = int(input("Enter a number: "))
    total = total+num
avg = total/10
print(f'Average of 10 numbers is {avg:.2f}')
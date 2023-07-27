#WAP to display all the numbers which are divisible by 11 but not by 2 between 100 and 500.

lower = int(input("Enter number starts from 100: "))
upper = int(input("Enter number ends at 500: "))
for num in range(lower,upper+1):
    if num%11 == 0 and num%2 !=0:
        print(num)

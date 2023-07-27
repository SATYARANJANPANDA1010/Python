# WAP to print table of a number accepted from the users in the following format
# input number - 10
# Expected Output format is : 10 * 1 = 10
#                             10 * 2  = 20
num = int(input("Enter a number: "))
for i in range(1,11):
    print(i,"*",num,"=",num*i)

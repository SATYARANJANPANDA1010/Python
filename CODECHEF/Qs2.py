# First and Last Digit
# CODECHEF --> https://www.codechef.com/problems/FLOW004?tab=statement
T = int(input("Enter Number of Test Cases: "))
for i in range(T):
    N = int(input("Enter Number: "))
    num_str = str(N)
    first_digit = int(num_str[0])
    last_digit = int(num_str[-1])
    sum_of_digit = first_digit + last_digit
    print(sum_of_digit)

def palindrome(num):
    temp=num
    rev=0
    while num>0:
        rem = num % 10
        rev = (rev * 10) + rem
        num = num // 10
    if rev == temp:
        print("palindrome number")
    else:
        print("not palindrome number")




n = int(input("Enter a number: "))
palindrome(n)
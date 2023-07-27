# WAP to find out the string is palindrome or not
str1 = input("Enter a string: ")
str2 = str1[::-1]
if str1 == str2:
    print("palindrome")
else:
    print("Not palindrome")
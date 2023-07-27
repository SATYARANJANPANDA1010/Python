# WAP to convert the string to upper case
str1 = input("Enter a string: ")
str2 = str() # create an empty string
for ch in str1:
    if ch>='a'and ch<='z':
        str2 = str2 + chr(ord(ch)-32)
    else:
        str2 = str2+ch
print(str2)
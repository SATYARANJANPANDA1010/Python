# WAP to convert all lower case letter to upper case and vice versa.
str1 = input("Enter a String: ")
str2 = str()
for ch in str1:
    if ch>='a' and ch<='z':
        str2 = str2+ chr(ord(ch)-32)
    else:
        str2 = str2 + chr(ord(ch)+32)
print(str1)
print(str2)

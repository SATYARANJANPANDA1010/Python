# str.rstrip()
str1 = "   abc"
str2 = "abc"
print(str1 == str2)
str3 = str1.lstrip()
print(str3)
print(str2 == str3)
s1 = "****NIT"
s2 = s1.lstrip("*")
print(s2)
s3 = "***n*i*t"
s4 = s3.lstrip("*")
print(s4)
s5 = "**$$%^nit"
s6 = s5.lstrip("*$%^")
print(s6)
s7 = "www.srpanda.com"
s8 = s7.lstrip('w.')
print(s8) 

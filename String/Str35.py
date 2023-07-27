# Find and replace method
# using IN operator
str1 = "python java python oracle"
print("java" in str1)
print(".net" in str1)
# using find method
i = str1.find("python")
print(i)
i1 = str1.rfind("java")
print(i1)
i2 = str1.find("mysql")
print(i2)
i3 = str1.find("python",5)
print(i3)
# "python" string is not lies between 5 to 10
i4 = str1.find("python",5,10)
print(i4)


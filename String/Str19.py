# str.rsplit()
str1 = "1,2,3,4,5,6"
l = str1.rsplit(",")
print(l)
# right to left split
l1 = str1.rsplit(",",2)
print(l1)
# left to right split
l2 = str1.split(",",2)
print(l2)



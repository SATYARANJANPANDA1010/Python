# str.split(sep= ,max split=-1)
str1 = '10,20,30,40,50,60'
l = str1.split(",")
print(l)
l1 = str1.split(",", 3)
print(l1)
str2 = '10 20 30 40 50 60'
l3 = str2.split()
print(l3)
l4 = str2.split(" ",2)
print(l4)

str5 = "1,2;3,4;5,6"
l5 = str5.split(';')
print(l5)
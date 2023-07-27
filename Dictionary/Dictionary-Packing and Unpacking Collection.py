#Packing and Unpacking Collection
a = 10
print(a)
print(type(a))
b = 10,20
print(b)
print(type(b))
a,b,c = 10,20,30
print(c)
#a,b,c = 10,20,30,40
#print(a,b,c)
#Output: ValueError: too many values to unpack (expected 3)

a,b,*c = 10,20,30,40,50
print(a,b,c)
#Output: 10 20 [30, 40, 50]

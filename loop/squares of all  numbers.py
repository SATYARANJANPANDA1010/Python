n = int(input("enter the values: "))
r = range(1,n+1)
s = 0
for i in r:
    print(f"{i} ---> {i**2}")
    s = s + (i**2)
print(f"sum of sqr is {s}")

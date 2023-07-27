#iter(d)
#using this iterator object we can iterate from dictionary

sales = {2020:45000,
         2021:50000,
         2023:80000}
a = iter(sales)
y1 = next(a)
y2 = next(a)
y3 = next(a)
print(y1,y2,y3)
print(sales[y1],sales[y2],sales[y3])
